#!/usr/bin/env python3
"""
Update latest commits and deployment activity in profile README
Shows real-time coding activity across repositories
"""

import os
import re
from datetime import datetime, timedelta
from typing import Dict, List
import requests
import pytz

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
GITHUB_USERNAME = 'brunoobueno'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Monitored repositories
MONITORED_REPOS = [
    'api-SofiaMed',
    'network-sentinel-dash',
    'erp-next-brasil',
    'dashboardLinx',
    'estoque-smart',
    'reliability-weaver',
    'business-leads-ai-automation',
    'cost-calculator-pro',
    'chatwoot-personalizado',
]


def get_latest_commits(limit: int = 5) -> List[Dict]:
    """Get latest commits across monitored repositories"""
    all_commits = []
    
    for repo in MONITORED_REPOS:
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/commits'
        params = {'per_page': 5}
        
        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=10)
            if response.status_code == 200:
                commits = response.json()
                for commit in commits[:3]:  # Top 3 per repo
                    commit_date = datetime.fromisoformat(
                        commit['commit']['author']['date'].replace('Z', '+00:00')
                    )
                    
                    all_commits.append({
                        'repo': repo,
                        'message': commit['commit']['message'].split('\n')[0][:60],
                        'sha': commit['sha'][:7],
                        'date': commit_date,
                        'url': commit['html_url']
                    })
        except Exception as e:
            print(f"Error fetching commits for {repo}: {e}")
    
    # Sort by date and get latest
    all_commits.sort(key=lambda x: x['date'], reverse=True)
    return all_commits[:limit]


def get_latest_releases() -> List[Dict]:
    """Get latest releases/tags across repositories"""
    releases = []
    
    for repo in MONITORED_REPOS:
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/releases/latest'
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                release = response.json()
                release_date = datetime.fromisoformat(
                    release['published_at'].replace('Z', '+00:00')
                )
                
                releases.append({
                    'repo': repo,
                    'tag': release['tag_name'],
                    'name': release['name'] or release['tag_name'],
                    'date': release_date,
                    'url': release['html_url']
                })
        except Exception as e:
            # No release found or error - skip
            pass
    
    releases.sort(key=lambda x: x['date'], reverse=True)
    return releases[:3]


def format_time_ago(date: datetime) -> str:
    """Format datetime as 'X hours/days ago'"""
    now = datetime.now(pytz.UTC)
    diff = now - date
    
    if diff.days > 0:
        return f"{diff.days}d ago"
    elif diff.seconds >= 3600:
        hours = diff.seconds // 3600
        return f"{hours}h ago"
    else:
        minutes = diff.seconds // 60
        return f"{minutes}m ago"


def generate_latest_commits_section(lang: str = 'en') -> str:
    """Generate latest commits section"""
    commits = get_latest_commits(5)
    
    if lang == 'pt':
        title = "### 🔥 Últimos Commits"
        if not commits:
            return f"{title}\n\n*Nenhum commit recente*\n"
    else:
        title = "### 🔥 Latest Commits"
        if not commits:
            return f"{title}\n\n*No recent commits*\n"
    
    lines = [title, ""]
    
    for commit in commits:
        time_ago = format_time_ago(commit['date'])
        emoji = "🎨" if "feat" in commit['message'].lower() else "🐛" if "fix" in commit['message'].lower() else "📝"
        
        lines.append(f"- {emoji} **[{commit['repo']}]({commit['url']})** - {commit['message']} `{time_ago}`")
    
    return '\n'.join(lines)


def generate_latest_releases_section(lang: str = 'en') -> str:
    """Generate latest releases section"""
    releases = get_latest_releases()
    
    if not releases:
        return ""
    
    if lang == 'pt':
        title = "### 🚀 Últimos Releases"
    else:
        title = "### 🚀 Latest Releases"
    
    lines = [title, ""]
    
    for release in releases:
        time_ago = format_time_ago(release['date'])
        lines.append(f"- 🎉 **[{release['repo']} {release['tag']}]({release['url']})** - {release['name']} `{time_ago}`")
    
    return '\n'.join(lines)


def update_readme_section(filepath: str, lang: str = 'en'):
    """Update the latest activity section in README"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate sections
    commits_section = generate_latest_commits_section(lang)
    releases_section = generate_latest_releases_section(lang)
    
    # Combined section
    new_section = f"""<!--START_LATEST_ACTIVITY-->
{commits_section}

{releases_section}
<!--END_LATEST_ACTIVITY-->"""
    
    # Check if markers exist
    if '<!--START_LATEST_ACTIVITY-->' in content:
        # Replace existing section
        pattern = r'<!--START_LATEST_ACTIVITY-->.*?<!--END_LATEST_ACTIVITY-->'
        updated_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    else:
        # Add before Recent Activity section
        if lang == 'pt':
            marker = "### ⚡ Atividade Recente"
        else:
            marker = "### ⚡ Recent Activity"
        
        if marker in content:
            updated_content = content.replace(
                marker,
                f"{new_section}\n\n{marker}"
            )
        else:
            # Fallback: add at the end of stats section
            updated_content = content
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Updated {filepath}")


def main():
    """Main execution"""
    print("🔄 Updating latest commits and releases...")
    
    # Update both READMEs
    update_readme_section('README.md', lang='pt')
    update_readme_section('README.en.md', lang='en')
    
    print("✨ Latest activity updated successfully!")


if __name__ == '__main__':
    main()
