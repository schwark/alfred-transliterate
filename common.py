import re

languages = {
    'as': { 'code': 'as', 'eng': 'Assamese', 'lng': 'অসমীয়া'},
    'bn': { 'code': 'bn', 'eng': 'Bengali', 'lng': 'বাংলা'},
    'gu': { 'code': 'gu', 'eng': 'Gujarati', 'lng': 'ગુજરાતી'},        
    'hi': { 'code': 'hi', 'eng': 'Hindi', 'lng': 'हिन्दी'},        
    'kn': { 'code': 'kn', 'eng': 'Kannada', 'lng': 'ಕನ್ನಡ'},        
    'ml': { 'code': 'ml', 'eng': 'Malayalam', 'lng': 'മലയാളം'},        
    'mr': { 'code': 'mr', 'eng': 'Marathi', 'lng': 'मराठी'},        
    'ne': { 'code': 'ne', 'eng': 'Nepali', 'lng': 'नेपाली'},        
    'or': { 'code': 'or', 'eng': 'Oriya', 'lng': 'ଓଡ଼ିଆ'},        
    'fa': { 'code': 'fa', 'eng': 'Persian', 'lng': 'پارسیان'},
    'pa': { 'code': 'pa', 'eng': 'Punjabi', 'lng': 'ਪੰਜਾਬੀ'},        
    'sa': { 'code': 'sa', 'eng': 'Sanskrit', 'lng': 'संस्कृतम्'},        
    'si': { 'code': 'si', 'eng': 'Sinhala', 'lng': 'සිංහල'},        
    'ta': { 'code': 'ta', 'eng': 'Tamil', 'lng': 'தமிழ்'},        
    'te': { 'code': 'te', 'eng': 'Telugu', 'lng': 'తెలుగు'},        
    'be': { 'code': 'be', 'eng': 'Belarusian', 'lng': 'беларуски'},     
    'bg': { 'code': 'bg', 'eng': 'Bulgarian', 'lng': 'български'},     
    'ru': { 'code': 'ru', 'eng': 'Russian', 'lng': 'русский'},     
    'sr': { 'code': 'sr', 'eng': 'Serbian', 'lng': 'српски'},     
    'uk': { 'code': 'uk', 'eng': 'Ukranian', 'lng': 'украї́нська'},     
    'ar': { 'code': 'ar', 'eng': 'Arabic', 'lng': 'عَرَبِيّ'},     
    'fa': { 'code': 'fa', 'eng': 'Persian', 'lng': 'فارسی'},     
    'ur': { 'code': 'ur', 'eng': 'Urdu', 'lng': 'اُردُو'},     
    'am': { 'code': 'am', 'eng': 'Amharic', 'lng': 'አማርኛ'},     
    'el': { 'code': 'el', 'eng': 'Greek', 'lng': 'ελληνικά'},     
    'he': { 'code': 'he', 'eng': 'Hebrew', 'lng': 'עִבְרִית'},     
    'ja': { 'code': 'ja', 'eng': 'Japanese', 'lng': '日本語'},     
    'th': { 'code': 'th', 'eng': 'Thai', 'lng': 'ภาษาไทย'},     
    'ti': { 'code': 'ti', 'eng': 'Tigrinya', 'lng': 'ትግርኛ'},     
    'zh': { 'code': 'zh', 'eng': 'Simplified Chinese', 'lng': '中国'},     
    'zh-hant': { 'code': 'zh-hant', 'eng': 'Traditional Chinese', 'lng': '中國'},     
    'yue-hant': { 'code': 'yue-hant', 'eng': 'Yue', 'lng': '中國'}
}

input_schemes = {
    "zh": [
        "pinyin",
        "pinyin-x0-shuangpin-abc",
        "pinyin-x0-shuangpin-ms",
        "pinyin-x0-shuangpin-flypy",
        "pinyin-x0-shuangpin-jiajia",
        "pinyin-x0-shuangpin-ziguang",
        "pinyin-x0-shuangpin-ziranma",
        "wubi-1986"
    ],
    "zh-hant": [
        "pinyin",
        "cangjie-1982"
    ],
    "yue-hant": [
        "jyutping",
        "und"
    ]
}
