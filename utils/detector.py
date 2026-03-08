#!/usr/bin/env python3

import re


class TechnologyDetector:
    def __init__(self):
        self.signatures = self._load_signatures()

    def _load_signatures(self):
        return {
            'cms': {
                'WordPress': {
                    'headers': ['wp-json', 'x-powered-by: wordpress'],
                    'meta':    ['wordpress'],
                    'scripts': ['wp-content', 'wp-includes'],
                    'html':    ['wp-content', 'wp-admin'],
                    'cookies': ['wordpress_', 'wp-settings'],
                },
                'Drupal': {
                    'headers': ['x-generator: drupal'],
                    'meta':    ['drupal'],
                    'html':    ['drupal.js', 'sites/all/'],
                    'cookies': ['drupal_'],
                },
                'Joomla': {
                    'meta':    ['joomla'],
                    'html':    ['joomla', 'media/jui/'],
                    'scripts': ['media/system/'],
                    'cookies': ['joomla_'],
                },
                'Magento': {
                    'html':    ['magento/', 'mage/'],
                    'cookies': ['frontend', 'adminhtml'],
                    'headers': ['x-magento-'],
                },
            },

            'web_servers': {
                'Apache': {
                    'headers': ['server: apache', 'x-powered-by: apache'],
                },
                'Nginx': {
                    'headers': ['server: nginx', 'x-powered-by: nginx'],
                },
                'IIS': {
                    'headers': ['server: microsoft-iis', 'x-powered-by: asp.net'],
                },
                'Cloudflare': {
                    'headers': ['server: cloudflare', 'cf-ray'],
                },
                'LiteSpeed': {
                    'headers': ['server: litespeed'],
                },
                'Caddy': {
                    'headers': ['server: caddy'],
                },
            },

            'javascript_frameworks': {
                'React': {
                    'scripts': ['react', 'react-dom'],
                    'html':    ['__reactinternalinstance', '__reactfiber', 'data-reactroot'],
                },
                'Vue.js': {
                    'scripts': ['vue.js', 'vue.min.js', '/vue@'],
                    'html':    ['v-bind:', 'v-on:', 'v-if=', 'v-for=', '__vue__'],
                },
                'Angular': {
                    'scripts': ['angular.js', 'angular.min.js', '/angular@'],
                    'html':    ['ng-app', 'ng-controller', 'ng-version'],
                },
                'Next.js': {
                    'html':    ['__next_data__', '_next/static'],
                    'scripts': ['/_next/'],
                },
                'Nuxt.js': {
                    'html':    ['__nuxt', 'data-n-head'],
                    'scripts': ['/_nuxt/'],
                },
                'jQuery': {
                    'scripts': ['jquery.js', 'jquery.min.js', '/jquery@'],
                },
                'Svelte': {
                    'html':    ['__svelte', 'svelte-'],
                },
                'Ember.js': {
                    'scripts': ['ember.js', 'ember.min.js'],
                    'html':    ['ember-application'],
                },
            },

            'programming_languages': {
                'PHP': {
                    'headers': ['x-powered-by: php'],
                    'cookies': ['phpsessid'],
                    'html':    ['.php'],
                },
                'Python': {
                    'headers': ['x-powered-by: python', 'server: wsgi', 'server: gunicorn',
                                'server: uvicorn'],
                    'cookies': ['sessionid', 'csrftoken'],
                },
                'Ruby': {
                    'headers': ['x-powered-by: ruby', 'x-runtime', 'server: webrick',
                                'server: puma', 'server: passenger'],
                    'cookies': ['_session_id'],
                },
                'Node.js': {
                    'headers': ['x-powered-by: express', 'server: node'],
                    'cookies': ['connect.sid'],
                },
                'ASP.NET': {
                    'headers': ['x-aspnet-version', 'x-aspnetmvc-version',
                                'x-powered-by: asp.net'],
                    'cookies': ['asp.net_sessionid', 'aspxauth'],
                },
            },

            'analytics': {
                'Google Analytics': {
                    'scripts': ['google-analytics.com/ga.js',
                                'google-analytics.com/analytics.js',
                                'gtag/js'],
                    'html':    ["ga('create'", "gtag('config'"],
                },
                'Google Tag Manager': {
                    'scripts': ['googletagmanager.com/gtm.js'],
                    'html':    ['googletagmanager.com/ns.html'],
                },
                'Facebook Pixel': {
                    'scripts': ['connect.facebook.net'],
                    'html':    ["fbq('init'", 'facebook pixel'],
                },
                'Hotjar': {
                    'scripts': ['static.hotjar.com'],
                    'html':    ['hotjar'],
                },
                'Matomo': {
                    'scripts': ['matomo.js', 'piwik.js'],
                    'html':    ["_paq.push"],
                },
            },

            'cdn': {
                'Cloudflare': {
                    'headers': ['server: cloudflare', 'cf-ray', 'cf-cache-status'],
                },
                'Amazon CloudFront': {
                    'headers': ['server: cloudfront', 'x-amz-cf-id', 'x-amz-cf-pop'],
                },
                'Akamai': {
                    'headers': ['x-akamai-transformed', 'akamai-grn', 'x-check-cacheable'],
                },
                'Fastly': {
                    'headers': ['x-fastly-request-id', 'x-served-by', 'x-cache: hit, hit'],
                },
                'jsDelivr': {
                    'scripts': ['cdn.jsdelivr.net'],
                },
                'Cloudinary': {
                    'html':    ['cloudinary.com', 'res.cloudinary.com'],
                },
            },

            'databases': {
                'MySQL': {
                    'html':    ['mysql_connect', 'mysqli_'],
                    'headers': ['x-db: mysql'],
                },
                'MongoDB': {
                    'html':    ['mongodb://', 'mongoose'],
                    'headers': ['x-db: mongodb'],
                },
                'PostgreSQL': {
                    'html':    ['pg_connect', 'psycopg2'],
                    'headers': ['x-db: postgresql'],
                },
                'Redis': {
                    'headers': ['x-redis', 'x-cache: redis'],
                },
                'Elasticsearch': {
                    'headers': ['x-elastic-product'],
                    'html':    ['elasticsearch'],
                },
            },

            'ecommerce': {
                'Shopify': {
                    'html':    ['shopify.com', 'cdn.shopify.com'],
                    'cookies': ['_shopify_'],
                },
                'WooCommerce': {
                    'html':    ['woocommerce', 'wc-cart'],
                    'scripts': ['woocommerce/'],
                },
                'PrestaShop': {
                    'html':    ['prestashop', 'prestashop.css'],
                    'cookies': ['prestashop-'],
                },
                'OpenCart': {
                    'html':    ['route=common/home', 'catalog/view/theme'],
                    'cookies': ['OCSESSID'],
                },
                'BigCommerce': {
                    'html':    ['bigcommerce.com', 'bc-sf-filter'],
                    'cookies': ['SHOP_SESSION_TOKEN'],
                },
                'Wix': {
                    'html':    ['wix.com', 'wixsite.com', 'wix-bolt'],
                    'scripts': ['static.wixstatic.com'],
                },
            },
        }


    def detect_all(self, website_data):
        """Run all detectors and return a merged, deduplicated results dict."""
        # Initialise with all expected keys so callers never get KeyErrors
        results = {
            'cms':                   [],
            'web_servers':           [],
            'javascript_frameworks': [],
            'programming_languages': [],
            'analytics':             [],
            'cdn':                   [],
            'databases':             [],
            'ecommerce':             [],
            'security':              [],
        }

        sources = [
            self._detect_from_headers(website_data['headers']),
            self._detect_from_html(website_data['content']),
            self._detect_from_cookies(website_data['cookies']),
            self._detect_from_scripts(website_data['content']),
            self._detect_security_headers(website_data['headers']),
        ]

        for source in sources:
            for category, items in source.items():
                for item in items:
                    if item not in results[category]:
                        results[category].append(item)

        return results

    def _detect_from_headers(self, headers):
        detected = {cat: [] for cat in self.signatures}
        lowered = {k.lower(): v.lower() for k, v in headers.items()}

        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                for pattern in patterns.get('headers', []):
                    pattern_l = pattern.lower()
                    # Pattern may be "header-name: value" or just a header name/fragment
                    if ':' in pattern_l:
                        name, _, val = pattern_l.partition(':')
                        name = name.strip()
                        val = val.strip()
                        if name in lowered and val in lowered[name]:
                            detected[category].append(tech)
                            break
                    else:
                        # Match as a substring of any header name
                        if any(pattern_l in hname for hname in lowered):
                            detected[category].append(tech)
                            break

        return detected

    def _detect_from_html(self, html_content):
        detected = {cat: [] for cat in self.signatures}
        html_lower = html_content.lower()

        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                matched = False

                for pattern in patterns.get('html', []):
                    if pattern.lower() in html_lower:
                        detected[category].append(tech)
                        matched = True
                        break

                if matched:
                    continue

                for pattern in patterns.get('meta', []):
                    meta_re = re.compile(
                        r'<meta[^>]+content=["\'][^"\']*' + re.escape(pattern) + r'[^"\']*["\']',
                        re.IGNORECASE
                    )
                    if meta_re.search(html_content):
                        detected[category].append(tech)
                        break

        return detected

    def _detect_from_cookies(self, cookies):
        detected = {cat: [] for cat in self.signatures}

        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                for pattern in patterns.get('cookies', []):
                    if any(pattern.lower() in name.lower() for name in cookies):
                        detected[category].append(tech)
                        break

        return detected

    def _detect_from_scripts(self, html_content):
        detected = {cat: [] for cat in self.signatures}

        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                for pattern in patterns.get('scripts', []):
                    script_re = re.compile(
                        r'<script[^>]+src=["\'][^"\']*' + re.escape(pattern) + r'[^"\']*["\']',
                        re.IGNORECASE
                    )
                    if script_re.search(html_content):
                        detected[category].append(tech)
                        break

        return detected

    def _detect_security_headers(self, headers):
        security_features = []

        security_headers = {
            'Content-Security-Policy':   'CSP Header',
            'X-Content-Type-Options':    'MIME Sniffing Protection',
            'X-Frame-Options':           'Clickjacking Protection',
            'X-XSS-Protection':          'XSS Protection',
            'Strict-Transport-Security': 'HSTS Enabled',
            'Referrer-Policy':           'Referrer Policy',
            'Permissions-Policy':        'Permissions Policy',
            'Cross-Origin-Opener-Policy':'COOP Header',
            'Cross-Origin-Embedder-Policy': 'COEP Header',
        }

        lowered = {k.lower(): (k, v) for k, v in headers.items()}

        for header, description in security_headers.items():
            original_key, value = lowered.get(header.lower(), (None, None))
            if value is not None:
                # Truncate very long header values for display
                display_val = value if len(value) <= 80 else value[:77] + '...'
                security_features.append(f"{description}: {display_val}")

        return {'security': security_features}
