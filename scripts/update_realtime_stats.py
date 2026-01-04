#!/usr/bin/env python3
"""
Real-time GitHub stats updater
Fetches live data from GitHub API and generates dynamic metrics
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List
import pytz

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
GITHUB_USERNAME = 'brunoobueno'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Repositories to track actively
ACTIVE_REPOS = [
    'erpnext-brasil', 'estoque-smart', 'api-SofiaMed', 
    'network-sentinel-dash', 'reliability-weaver',
    'dashboardLinx', 'business-leads-ai-automation'
]


def get_user_stats() -> Dict:
    """Get overall user statistics"""
    url = f'https://api.github.com/users/{GITHUB_USERNAME}'
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                'public_repos': data.get('public_repos', 0),
                'followers': data.get('followers', 0),
                'following': data.get('following', 0),
                'created_at': data.get('created_at', ''),
            }
    except Exception as e:
        print(f"Error fetching user stats: {e}")
    
    return {}


def get_recent_commits(days: int = 7) -> List[Dict]:
    """Get recent commits across all repos"""
    since = (datetime.now(pytz.UTC) - timedelta(days=days)).isoformat()
    commits = []
    
    for repo in ACTIVE_REPOS:
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/commits'
        params = {'since': since, 'per_page': 10}
        
        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=10)
            if response.status_code == 200:
                repo_commits = response.json()
                for commit in repo_commits:
                    commits.append({
                        'repo': repo,
                        'message': commit['commit']['message'].split('\n')[0],
                        'date': commit['commit']['author']['date'],
                        'sha': commit['sha'][:7]
                    })
        except Exception as e:
            print(f"Error fetching commits for {repo}: {e}")
    
    # Sort by date
    commits.sort(key=lambda x: x['date'], reverse=True)
    return commits[:10]  # Top 10


def get_active_projects() -> List[Dict]:
    """Get currently active projects based on recent pushes"""
    active = []
    cutoff = datetime.now(pytz.UTC) - timedelta(days=7)
    
    for repo in ACTIVE_REPOS:
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo}'
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                data = response.json()
                pushed_at = datetime.fromisoformat(data['pushed_at'].replace('Z', '+00:00'))
                
                if pushed_at > cutoff:
                    active.append({
                        'name': repo,
                        'last_push': data['pushed_at'],
                        'language': data.get('language', 'Unknown'),
                        'description': data.get('description', ''),
                        'stars': data.get('stargazers_count', 0)
                    })
        except Exception as e:
            print(f"Error fetching repo {repo}: {e}")
    
    active.sort(key=lambda x: x['last_push'], reverse=True)
    return active


def get_contribution_stats() -> Dict:
    """Get contribution statistics"""
    # Get events (last 90 days of activity)
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/events/public'
    
    event_types = {
        'PushEvent': 0,
        'PullRequestEvent': 0,
        'IssuesEvent': 0,
        'CreateEvent': 0
    }
    
    try:
        response = requests.get(url, headers=HEADERS, params={'per_page': 100}, timeout=10)
        if response.status_code == 200:
            events = response.json()
            for event in events:
                event_type = event.get('type')
                if event_type in event_types:
                    event_types[event_type] += 1
    except Exception as e:
        print(f"Error fetching events: {e}")
    
    return {
        'commits_pushed': event_types['PushEvent'],
        'pull_requests': event_types['PullRequestEvent'],
        'issues': event_types['IssuesEvent'],
        'repos_created': event_types['CreateEvent']
    }


def generate_stats_json():
    """Generate JSON with all stats"""
    stats = {
        'updated_at': datetime.now(pytz.UTC).isoformat(),
        'user': get_user_stats(),
        'recent_commits': get_recent_commits(),
        'active_projects': get_active_projects(),
        'contributions': get_contribution_stats()
    }
    
    # Ensure stats directory exists
    os.makedirs('stats', exist_ok=True)
    
    # Write JSON
    with open('stats/realtime.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Stats updated at {stats['updated_at']}")
    return stats


def generate_stats_svg(stats: Dict):
    """Generate SVG badge with current stats"""
    
    active_count = len(stats['active_projects'])
    recent_commits = len(stats['recent_commits'])
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="120" viewBox="0 0 400 120">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#58A6FF;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1F6FEB;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <rect width="400" height="120" fill="#0D1117" rx="10"/>
  <rect width="400" height="40" fill="url(#grad)" rx="10"/>
  
  <text x="200" y="25" font-family="Arial" font-size="16" fill="white" text-anchor="middle" font-weight="bold">
    🔥 Live Activity
  </text>
  
  <text x="100" y="65" font-family="Arial" font-size="14" fill="#C9D1D9" text-anchor="middle">
    Active Projects
  </text>
  <text x="100" y="90" font-family="Arial" font-size="24" fill="#58A6FF" text-anchor="middle" font-weight="bold">
    {active_count}
  </text>
  
  <text x="300" y="65" font-family="Arial" font-size="14" fill="#C9D1D9" text-anchor="middle">
    Commits (7d)
  </text>
  <text x="300" y="90" font-family="Arial" font-size="24" fill="#1F6FEB" text-anchor="middle" font-weight="bold">
    {recent_commits}
  </text>
  
  <text x="200" y="110" font-family="Arial" font-size="10" fill="#8B949E" text-anchor="middle">
    Updated: {datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M UTC')}
  </text>
</svg>'''
    
    with open('stats/live-activity.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    
    print("✅ SVG badge generated")


def main():
    """Main execution"""
    print("🔄 Fetching real-time GitHub stats...")
    
    stats = generate_stats_json()
    generate_stats_svg(stats)
    
    print(f"""
📊 Stats Summary:
- Public Repos: {stats['user'].get('public_repos', 'N/A')}
- Active Projects: {len(stats['active_projects'])}
- Recent Commits: {len(stats['recent_commits'])}
- Contributions: {stats['contributions'].get('commits_pushed', 0)} pushes
    """)
    
    print("✨ Real-time stats updated successfully!")


if __name__ == '__main__':
    main()
