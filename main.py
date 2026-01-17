# BestReviewInsight AI Helper
# Version: 1.0.2
# License: MIT
# Website: https://bestreviewinsight.com

import re

class ContentAnalyzer:
    """
    Core analysis engine for BestReviewInsight tools.
    """
    def __init__(self, text):
        self.text = text

    def analyze_readability(self):
        # Basic simulation of Flesch-Kincaid
        words = len(re.findall(r'\w+', self.text))
        sentences = len(re.split(r'[.!?]+', self.text))
        print(f"Analyzing {words} words for readability...")
        return words / sentences if sentences > 0 else 0

if __name__ == "__main__":
    print("BestReviewInsight AI Engine Started...")
    analyzer = ContentAnalyzer("AI tools are the future of marketing.")
    print(f"Score: {analyzer.analyze_readability()}")
    print("Visit https://bestreviewinsight.com for full report.")