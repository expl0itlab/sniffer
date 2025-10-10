#!/usr/bin/env python3

import re
import json

class TechnologyDetector:
    def __init__(self):
        self.signatures = self.load_signatures()
    
    def load_signatures(self):
        return {
            'cms': {
                'WordPress': {
                    'headers': ['wp-json', 'x-powered-by: wordpress'],
                    'meta': ['generator', 'wordpress'],
                    'scripts': ['wp-content', 'wp-includes'],
                    'html': ['wp-content', 'wp-admin'],
                    'cookies': ['wordpress_', 'wp-settings']
                },
                'Drupal': {
                    'headers': ['x-generator: drupal'],
                    'meta': ['generator', 'drupal'],
                    'html': ['drupal.js', 'sites/all/'],
                    'cookies': ['drupal_']
                },
                'Joomla': {
                    'meta': ['generator', 'joomla'],
                    'html': ['joomla', 'media/jui/'],
                    'scripts': ['media/system/'],
                    'cookies': ['joomla_']
                },
                'Magento': {
                    'html': ['magento/', 'mage/'],
                    'cookies': ['frontend', 'adminhtml'],
                    'headers': ['x-magento-']
                }
            },
            
            'web_servers': {
                'Apache': {
                    'headers': ['server: apache', 'x-powered-by: apache']
                },
                'Nginx': {
                    'headers': ['server: nginx', 'x-powered-by: nginx']
                },
                'IIS': {
                    'headers': ['server: microsoft-iis', 'x-powered-by: asp.net']
                },
                'Cloudflare': {
                    'headers': ['server: cloudflare', 'cf-ray']
                }
            },
            
            'javascript_frameworks': {
                'React': {
                    'scripts': ['react', 'react-dom'],
                    'html': ['__reactInternalInstance'],
                    'global_vars': ['React', 'ReactDOM']
                },
                'Vue.js': {
                    'scripts': ['vue', 'vue.js'],
                    'html': ['v-bind', 'v-on'],
                    'global_vars': ['Vue']
                },
                'Angular': {
                    'scripts': ['angular', 'ng-'],
                    'html': ['ng-app', 'ng-controller'],
                    'global_vars': ['angular']
                },
                'jQuery': {
                    'scripts': ['jquery'],
                    'global_vars': ['jQuery', '$']
                }
            },
            
            'programming_languages': {
                'PHP': {
                    'headers': ['x-powered-by: php'],
                    'cookies': ['phpsessid'],
                    'html': ['.php']
                },
                'Python': {
                    'headers': ['x-powered-by: python', 'server: wsgi'],
                    'cookies': ['sessionid', 'csrftoken']
                },
                'Ruby': {
                    'headers': ['x-powered-by: ruby', 'x-runtime', 'server: webrick'],
                    'cookies': ['_session_id']
                },
                'Node.js': {
                    'headers': ['x-powered-by: express', 'server: node'],
                    'cookies': ['connect.sid']
                }
            },
            
            'analytics': {
                'Google Analytics': {
                    'scripts': ['google-analytics.com/ga.js', 'gtag.js', 'analytics.js'],
                    'html': ['ga(\'create\'', 'gtag(\'config\'']
                },
                'Google Tag Manager': {
                    'scripts': ['googletagmanager.com/gtm.js'],
                    'html': ['noscript><iframe src="//www.googletagmanager.com/ns.html']
                },
                'Facebook Pixel': {
                    'scripts': ['facebook.net/pixel.js'],
                    'html': ['fbq(\'init\'', 'facebook pixel']
                }
            },
            
            'cdn': {
                'Cloudflare': {
                    'headers': ['server: cloudflare', 'cf-ray'],
                    'dns': ['cloudflare.com']
                },
                'Amazon CloudFront': {
                    'headers': ['server: cloudfront', 'x-amz-cf-'],
                    'dns': ['cloudfront.net']
                },
                'Akamai': {
                    'headers': ['server: akamai'],
                    'dns': ['akamai.net', 'akamaiedge.net']
                }
            },
            
            'ecommerce': {
                'Shopify': {
                    'html': ['shopify.com', 'cdn.shopify.com'],
                    'cookies': ['_shopify_']
                },
                'WooCommerce': {
                    'html': ['woocommerce', 'wc-'],
                    'scripts': ['woocommerce/']
                },
                'PrestaShop': {
                    'html': ['prestashop', 'prestashop.css'],
                    'cookies': ['prestashop-']
                }
            }
        }
    
    def detect_all(self, website_data):
        results = {
            'cms': [],
            'web_servers': [],
            'javascript_frameworks': [],
            'programming_languages': [],
            'analytics': [],
            'cdn': [],
            'databases': [],
            'ecommerce': [],
            'security': []
        }
        
        results.update(self.detect_from_headers(website_data['headers']))
        results.update(self.detect_from_html(website_data['content']))
        results.update(self.detect_from_cookies(website_data['cookies']))
        results.update(self.detect_from_scripts(website_data['content']))
        results.update(self.detect_security_headers(website_data['headers']))
        
        return results
    
    def detect_from_headers(self, headers):
        detected = {category: [] for category in self.signatures.keys()}
        
        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                if 'headers' in patterns:
                    for pattern in patterns['headers']:
                        for header_name, header_value in headers.items():
                            header_str = f"{header_name.lower()}: {header_value.lower()}"
                            if pattern.lower() in header_str:
                                detected[category].append(tech)
                                break
        
        return detected
    
    def detect_from_html(self, html_content):
        detected = {category: [] for category in self.signatures.keys()}
        html_lower = html_content.lower()
        
        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                if 'html' in patterns:
                    for pattern in patterns['html']:
                        if pattern.lower() in html_lower:
                            detected[category].append(tech)
                            break
                
                if 'meta' in patterns:
                    for pattern in patterns['meta']:
                        meta_pattern = f'meta.*{pattern}'
                        if re.search(meta_pattern, html_lower, re.IGNORECASE):
                            detected[category].append(tech)
                            break
        
        return detected
    
    def detect_from_cookies(self, cookies):
        detected = {category: [] for category in self.signatures.keys()}
        
        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                if 'cookies' in patterns:
                    for pattern in patterns['cookies']:
                        for cookie_name in cookies.keys():
                            if pattern.lower() in cookie_name.lower():
                                detected[category].append(tech)
                                break
        
        return detected
    
    def detect_from_scripts(self, html_content):
        detected = {category: [] for category in self.signatures.keys()}
        
        for category, technologies in self.signatures.items():
            for tech, patterns in technologies.items():
                if 'scripts' in patterns:
                    for pattern in patterns['scripts']:
                        script_pattern = f'script.*{pattern}'
                        if re.search(script_pattern, html_content, re.IGNORECASE):
                            detected[category].append(tech)
                            break
                
                if 'global_vars' in patterns:
                    for pattern in patterns['global_vars']:
                        var_pattern = f'var {pattern}|{pattern}\.='
                        if re.search(var_pattern, html_content):
                            detected[category].append(tech)
                            break
        
        return detected
    
    def detect_security_headers(self, headers):
        security_features = []
        
        security_headers = {
            'Content-Security-Policy': 'CSP Header',
            'X-Content-Type-Options': 'MIME Sniffing Protection',
            'X-Frame-Options': 'Clickjacking Protection',
            'X-XSS-Protection': 'XSS Protection',
            'Strict-Transport-Security': 'HSTS Enabled',
            'Referrer-Policy': 'Referrer Policy',
            'Feature-Policy': 'Feature Policy',
            'Permissions-Policy': 'Permissions Policy'
        }
        
        for header, description in security_headers.items():
            if header in headers:
                security_features.append(f"{description}: {headers[header]}")
        
        return {'security': security_features}