#!/usr/bin/env python3
"""
API Roulette: Because sometimes the API is just playing hard to get.

When your API calls keep failing, this tool helps you stop banging your head
against the same broken endpoint. It's like Russian roulette, but with HTTP
status codes instead of bullets.
"""

import requests
import time
import random
from datetime import datetime

def api_roulette(url, max_attempts=5, timeout=10):
    """
    Play API roulette! Will you get a 200 or join the 500 club?
    
    Args:
        url: The endpoint that's probably ignoring your calls
        max_attempts: How many times to humiliate yourself before giving up
        timeout: How long to wait before realizing they're just not that into you
    
    Returns:
        The response if successful, None if you should probably take a coffee break
    """
    
    headers = {
        'User-Agent': 'API Roulette/1.0 (Please work, please work)'
    }
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n🎰 Attempt {attempt}/{max_attempts}: Spinning the roulette wheel...")
        
        try:
            # The moment of truth - will it be love or heartbreak?
            response = requests.get(url, headers=headers, timeout=timeout)
            
            print(f"   Status: {response.status_code} - {"Success!" if response.ok else "API says no"}")
            print(f"   Time: {datetime.now().strftime('%H:%M:%S')}")
            
            if response.ok:
                print(f"🎉 Winner winner! API actually responded!")
                return response
            
            # Handle rate limiting like a polite developer
            if response.status_code == 429:
                retry_after = response.headers.get('Retry-After', 5)
                print(f"⏰ Rate limited! API needs {retry_after}s to think about what it's done")
                time.sleep(int(retry_after))
                continue
                
        except requests.exceptions.Timeout:
            print(f"⏰ Timeout! The API is taking a long lunch break")
        except requests.exceptions.ConnectionError:
            print(f"🔌 Connection error! Did someone unplug the server?")
        except Exception as e:
            print(f"🤷 Unexpected error: {e}")
        
        # Exponential backoff with a dash of randomness
        wait_time = min(2 ** attempt + random.uniform(0, 1), 30)
        print(f"💤 Sleeping for {wait_time:.1f}s before trying again...")
        time.sleep(wait_time)
    
    print(f"\n💀 All {max_attempts} attempts failed. Maybe the API ghosted you?")
    print(f"   Try: 1) Check your URL 2) Check the service status 3) Go pet a dog")
    return None

if __name__ == "__main__":
    # Example usage - replace with your problematic API
    print("🔫 API ROULETTE - WILL YOUR REQUEST SURVIVE?")
    print("=" * 50)
    
    # Try a test endpoint (or replace with your own)
    test_url = "https://httpbin.org/status/200"  # Change to /status/429 or /delay/5 for fun
    
    result = api_roulette(test_url)
    
    if result:
        print(f"\n📦 Response preview: {result.text[:100]}...")
    else:
        print("\n😭 Better luck next time!")
