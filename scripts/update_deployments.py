#!/usr/bin/env python3
"""
Auto-update deployment status in profile README
Fetches latest activity from GitHub repos and updates deployment section
"""

import os
import re
from datetime import datetime, timedelta
from typing import Dict, List
import requests

# GitHub API configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
GITHUB_USERNAME = 'brunoobueno'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Repository monitoring configuration
PRODUCTION_REPOS = {
    'erpnext-brasil': 'Industrial ERP',
    'smtp-alquimia': 'Email Infrastructure',
    'estoque-smart': 'Inventory System',
    'dashboardLinx': 'Analytics Platform',
}

BETA_REPOS = {
    'api-SofiaMed': 'Healthcare AI',
    'cost-calculator-pro': 'Cost Analysis',
}

RESEARCH_REPOS = {
    'network-sentinel-dash': 'Security Research',
    'reliability-weaver': 'ML Models',
}


def get_repo_activity(repo_name: str) -> Dict:
    """Get latest activity for a repository"""
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/commits'
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            commits = response.json()
            if commits:
                latest_commit = commits[0]
                return {
                    'last_updated': latest_commit['commit']['author']['date'],
                    'active': True
                }
    except Exception as e:
        print(f"Error fetching {repo_name}: {e}")
    
    return {'active': False}


def check_recent_activity(last_updated: str, days: int = 30) -> bool:
    """Check if repo had activity in last N days"""
    try:
        commit_date = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
        return (datetime.now(commit_date.tzinfo) - commit_date).days < days
    except:
        return False


def generate_deployment_section(lang: str = 'en') -> str:
    """Generate the deployment status section"""
    
    if lang == 'pt':
        section_title = "## 🔄 Últimos Deploys"
        prod_label = "Ambientes de Produção:"
        beta_label = "Releases Beta:"
        research_label = "Pesquisa:"
        status_active = "Ativo"
        status_testing = "Testes"
        status_dev = "Dev"
        status_training = "Treinamento"
    else:
        section_title = "## 🔄 Latest Deployments"
        prod_label = "Production Environments:"
        beta_label = "Beta Releases:"
        research_label = "Research:"
        status_active = "Active"
        status_testing = "Testing"
        status_dev = "Dev"
        status_training = "Training"
    
    lines = [section_title, "", "```yaml"]
    
    # Production
    lines.append(prod_label)
    for repo, desc in PRODUCTION_REPOS.items():
        activity = get_repo_activity(repo)
        status = status_active if activity['active'] else "Inactive"
        lines.append(f"  - {repo:24} → {desc} ({status})")
    
    lines.append("")
    
    # Beta
    lines.append(beta_label)
    for repo, desc in BETA_REPOS.items():
        activity = get_repo_activity(repo)
        status = status_testing if activity['active'] else "Paused"
        lines.append(f"  - {repo:24} → {desc} ({status})")
    
    lines.append("")
    
    # Research
    lines.append(research_label)
    research_statuses = {
        'network-sentinel-dash': status_dev,
        'reliability-weaver': status_training
    }
    for repo, desc in RESEARCH_REPOS.items():
        status = research_statuses.get(repo, status_dev)
        lines.append(f"  - {repo:24} → {desc} ({status})")
    
    lines.append("```")
    
    return '\n'.join(lines)


def update_readme(filepath: str, lang: str = 'en'):
    """Update README with new deployment section"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new section
    new_section = generate_deployment_section(lang)
    
    # Pattern to match the deployment section
    if lang == 'pt':
        pattern = r'## 🔄 Últimos Deploys\n\n```yaml.*?```'
    else:
        pattern = r'## 🔄 Latest Deployments\n\n```yaml.*?```'
    
    # Replace the section
    updated_content = re.sub(
        pattern,
        new_section,
        content,
        flags=re.DOTALL
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Updated {filepath}")


def main():
    """Main execution"""
    print("🔄 Updating deployment status...")
    
    # Update English README
    update_readme('README.md', lang='en')
    
    # Update Portuguese README
    update_readme('README.pt-BR.md', lang='pt')
    
    print("✨ Deployment status updated successfully!")


if __name__ == '__main__':
    main()
