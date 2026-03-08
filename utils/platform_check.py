#!/usr/bin/env python3

import os
import sys
import platform
import subprocess

from utils.banner import print_info, print_warning, print_error, print_success


def check_python_version():
    if sys.version_info < (3, 6):
        print_error("Python 3.6 or higher is required")
        sys.exit(1)
    print_success(f"Python version: {platform.python_version()}")


def check_required_packages():
    required_packages = ['requests', 'colorama']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print_warning(f"Missing packages: {', '.join(missing_packages)}")
        install_choice = input("Install missing packages? (y/n): ").strip().lower()
        if install_choice in ['y', 'yes']:
            _install_packages(missing_packages)
        else:
            print_error("Required packages missing. Exiting.")
            sys.exit(1)
    else:
        print_success("All required packages are installed")


def _install_packages(packages):
    for package in packages:
        try:
            print_info(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print_success(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print_error(f"Failed to install {package}")
            sys.exit(1)


def check_platform_requirements():
    print_info("Checking system requirements...")
    check_python_version()
    check_required_packages()
    _check_user_environment()
    print_success("System requirements check completed")


def _check_user_environment():
    current_platform = platform.system()
    is_termux = 'termux' in os.environ.get('PREFIX', '').lower()

    if current_platform != 'Windows':
        is_root = os.geteuid() == 0
        if is_root:
            print_warning("Running as root user")
    else:
        print_info(f"Platform: Windows")

    if is_termux:
        print_info("Termux environment detected")
        if not _check_termux_requirements():
            setup_choice = input("Setup Termux requirements? (y/n): ").strip().lower()
            if setup_choice in ['y', 'yes']:
                _setup_termux_environment()
    elif current_platform != 'Windows':
        print_info(f"Platform: {current_platform}")


def _check_termux_requirements():
    try:
        result = subprocess.run(
            ['pkg', 'list-installed'],
            capture_output=True,
            text=True
        )
        required_pkgs = ['python', 'git']
        missing = [p for p in required_pkgs if p not in result.stdout]

        if missing:
            print_warning(f"Missing Termux packages: {', '.join(missing)}")
            return False
        return True

    except Exception as e:
        print_warning(f"Could not verify Termux packages: {e}")
        return False


def _setup_termux_environment():
    try:
        print_info("Setting up Termux environment...")
        subprocess.run(['pkg', 'update',  '-y'], check=True)
        subprocess.run(['pkg', 'upgrade', '-y'], check=True)
        subprocess.run(['pkg', 'install', '-y', 'python', 'git'], check=True)
        print_success("Termux environment setup completed")
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to setup Termux environment: {e}")
        sys.exit(1)
