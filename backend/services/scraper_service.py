import requests
from bs4 import BeautifulSoup
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class ArticleScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def scrape_article_content(self, url: str) -> Optional[str]:
        """
        Scrape the full content of an article from its URL
        """
        try:
            logger.info(f"Scraping article from: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try different common article content selectors
            content_selectors = [
                'article',
                '.article-content',
                '.post-content',
                '.entry-content',
                '.content',
                'div[itemprop="articleBody"]',
                '.story-body',
                '.article-body'
            ]
            
            content = None
            for selector in content_selectors:
                elements = soup.select(selector)
                if elements:
                    # Get all paragraphs from the article
                    paragraphs = elements[0].find_all('p')
                    if paragraphs:
                        content = '\n\n'.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
                        break
            
            # Fallback: try to get all paragraphs from the page
            if not content:
                paragraphs = soup.find_all('p')
                if len(paragraphs) > 3:  # At least 3 paragraphs to be considered article content
                    content = '\n\n'.join([p.get_text().strip() for p in paragraphs[:15] if p.get_text().strip()])
            
            if content and len(content) > 200:
                logger.info(f"Successfully scraped {len(content)} characters")
                return content
            else:
                logger.warning(f"Could not extract meaningful content from {url}")
                return None
                
        except Exception as e:
            logger.error(f"Error scraping article from {url}: {str(e)}")
            return None
    
    def enhance_article(self, article: Dict) -> Dict:
        """
        Enhance an article with scraped full content
        """
        if article.get('url') and article.get('content'):
            # Only scrape if current content is short (likely truncated)
            if len(article['content']) < 500:
                full_content = self.scrape_article_content(article['url'])
                if full_content:
                    article['full_content'] = full_content
                    article['content'] = full_content
        return article
