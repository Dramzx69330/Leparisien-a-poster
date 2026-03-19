#!/usr/bin/env python3
"""
Backend API Testing for Le Parisien Clone
Tests all news API endpoints for proper functionality and response structure
"""

import requests
import json
import os
import sys
from datetime import datetime
from typing import Dict, Any

# Get backend URL from environment
BACKEND_URL = "https://market-intel-137.preview.emergentagent.com/api"

# Required fields for articles
REQUIRED_ARTICLE_FIELDS = [
    'id', 'title', 'excerpt', 'image', 'url', 
    'source', 'publishedAt', 'timestamp', 'readTime'
]

def log_test_result(endpoint: str, success: bool, details: str, response_data: Dict = None):
    """Log test results with timestamp"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {status} {endpoint}")
    print(f"Details: {details}")
    if response_data and not success:
        print(f"Response: {json.dumps(response_data, indent=2)[:500]}...")

def validate_article_structure(article: Dict) -> tuple[bool, str]:
    """Validate that article has all required fields"""
    missing_fields = []
    for field in REQUIRED_ARTICLE_FIELDS:
        if field not in article:
            missing_fields.append(field)
    
    if missing_fields:
        return False, f"Missing required fields: {missing_fields}"
    
    # Check field types
    if not isinstance(article.get('id'), (int, str)) or not article.get('id'):
        return False, "ID field is invalid or empty"
    
    if not isinstance(article.get('title'), str) or not article.get('title').strip():
        return False, "Title field is invalid or empty"
    
    return True, "Article structure is valid"

def validate_response_structure(response: Dict) -> tuple[bool, str]:
    """Validate standard response structure"""
    if 'status' not in response:
        return False, "Missing 'status' field in response"
    
    if response.get('status') != 'ok':
        return False, f"Response status is not 'ok': {response.get('status')}"
    
    if 'articles' not in response:
        return False, "Missing 'articles' field in response"
    
    if not isinstance(response.get('articles'), list):
        return False, "'articles' field is not a list"
    
    if 'totalResults' not in response:
        return False, "Missing 'totalResults' field in response"
    
    return True, "Response structure is valid"

def test_endpoint(endpoint: str, expected_min_articles: int = 1) -> tuple[bool, Dict]:
    """Test a single endpoint"""
    try:
        print(f"\n🔍 Testing: GET {endpoint}")
        response = requests.get(f"{BACKEND_URL}{endpoint}", timeout=30)
        
        # Check status code
        if response.status_code != 200:
            log_test_result(endpoint, False, f"HTTP {response.status_code}: {response.text}")
            return False, {"error": f"HTTP {response.status_code}", "text": response.text}
        
        # Parse JSON
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            log_test_result(endpoint, False, f"Invalid JSON response: {str(e)}")
            return False, {"error": "Invalid JSON", "text": response.text[:200]}
        
        # Validate response structure
        structure_valid, structure_msg = validate_response_structure(data)
        if not structure_valid:
            log_test_result(endpoint, False, structure_msg, data)
            return False, data
        
        articles = data.get('articles', [])
        
        # Check if we have articles when expected
        if expected_min_articles > 0 and len(articles) < expected_min_articles:
            log_test_result(endpoint, False, f"Expected at least {expected_min_articles} articles, got {len(articles)}", data)
            return False, data
        
        # Validate article structures
        for i, article in enumerate(articles[:3]):  # Check first 3 articles
            article_valid, article_msg = validate_article_structure(article)
            if not article_valid:
                log_test_result(endpoint, False, f"Article {i+1} validation failed: {article_msg}", article)
                return False, data
        
        log_test_result(endpoint, True, f"Success! Got {len(articles)} articles, totalResults: {data.get('totalResults')}")
        return True, data
        
    except requests.exceptions.Timeout:
        log_test_result(endpoint, False, "Request timeout (30s)")
        return False, {"error": "timeout"}
    except requests.exceptions.ConnectionError:
        log_test_result(endpoint, False, "Connection error - backend may be down")
        return False, {"error": "connection_error"}
    except Exception as e:
        log_test_result(endpoint, False, f"Unexpected error: {str(e)}")
        return False, {"error": str(e)}

def run_all_tests():
    """Run all backend API tests"""
    print("=" * 60)
    print("🚀 LE PARISIEN CLONE - BACKEND API TESTING")
    print("=" * 60)
    print(f"Backend URL: {BACKEND_URL}")
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    test_results = {}
    
    # Test 1: Top Headlines
    print(f"\n{'='*50}")
    print("TEST 1: Top Headlines")
    print(f"{'='*50}")
    success, data = test_endpoint("/news/top-headlines")
    test_results["top_headlines"] = {"success": success, "data": data}
    
    # Test 2: Search with France query  
    print(f"\n{'='*50}")
    print("TEST 2: Search News (France)")
    print(f"{'='*50}")
    success, data = test_endpoint("/news/search?q=France")
    test_results["search_france"] = {"success": success, "data": data}
    
    # Test 3: Recent news
    print(f"\n{'='*50}")
    print("TEST 3: Recent News")
    print(f"{'='*50}")
    success, data = test_endpoint("/news/recent")
    test_results["recent_news"] = {"success": success, "data": data}
    
    # Test 4: Sports category
    print(f"\n{'='*50}")
    print("TEST 4: Sports Category")
    print(f"{'='*50}")
    success, data = test_endpoint("/news/category/sports")
    test_results["sports_category"] = {"success": success, "data": data}
    
    # Test 5: Search with pagination
    print(f"\n{'='*50}")
    print("TEST 5: Search with Pagination")
    print(f"{'='*50}")
    success, data = test_endpoint("/news/search?q=Paris&page=1&pageSize=5")
    test_results["search_pagination"] = {"success": success, "data": data}
    
    # Summary
    print(f"\n{'='*60}")
    print("🏁 TEST SUMMARY")
    print(f"{'='*60}")
    
    passed_tests = []
    failed_tests = []
    
    for test_name, result in test_results.items():
        if result["success"]:
            passed_tests.append(test_name)
            print(f"✅ {test_name.replace('_', ' ').title()}")
        else:
            failed_tests.append(test_name)
            print(f"❌ {test_name.replace('_', ' ').title()}")
            if "error" in result["data"]:
                print(f"   Error: {result['data']['error']}")
    
    print(f"\n📊 Results: {len(passed_tests)}/{len(test_results)} tests passed")
    
    if failed_tests:
        print(f"\n⚠️  Failed tests: {', '.join(failed_tests)}")
        print("\n🔧 Debugging Information:")
        for test_name in failed_tests:
            result = test_results[test_name]
            print(f"\n{test_name}:")
            if isinstance(result["data"], dict):
                print(json.dumps(result["data"], indent=2)[:300] + "...")
    
    return len(passed_tests) == len(test_results), test_results

if __name__ == "__main__":
    try:
        all_passed, results = run_all_tests()
        
        print(f"\n{'='*60}")
        print("🎯 FINAL RESULT")
        print(f"{'='*60}")
        
        if all_passed:
            print("🎉 ALL TESTS PASSED! Backend APIs are working correctly.")
            sys.exit(0)
        else:
            print("❌ SOME TESTS FAILED. Check the details above.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n💥 Unexpected error during testing: {str(e)}")
        sys.exit(1)