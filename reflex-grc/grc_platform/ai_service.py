"""Google Gemini AI service for GRC analysis"""
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class GeminiAIService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if GOOGLE_API_KEY:
            genai.configure(api_key=GOOGLE_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
    
    def get_risk_suggestions(self, industry: str = "General") -> list:
        """Get AI-powered top 10 risk suggestions"""
        if not self.model:
            return self._get_fallback_risks()
        
        try:
            prompt = f"""As a GRC expert, suggest top 10 risks for {industry} industry.
            
Return ONLY a valid JSON array with this exact structure:
[
  {{
    "name": "Risk Name",
    "description": "Brief description",
    "category": "Category",
    "inherent_score": 7.5
  }}
]

Ensure inherent_score is between 1-10. Return only the JSON array, no other text."""
            
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            # Clean markdown code blocks if present
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            
            risks = json.loads(text)
            return risks[:10]  # Ensure only 10
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self._get_fallback_risks()
    
    async def analyze_risk_kri(self, context: dict) -> dict:
        """Analyze Risk-KRI-KCI relationships"""
        if not self.model:
            return self._get_fallback_analysis()
        
        try:
            prompt = f"""Analyze this GRC data:
            
Context: {json.dumps(context, indent=2)}

Provide analysis of KRI effectiveness and recommendations.

Return ONLY valid JSON:
{{
  "analysis": "Your detailed analysis here",
  "recommendations": ["rec1", "rec2", "rec3"]
}}"""
            
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            
            result = json.loads(text)
            return result
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self._get_fallback_analysis()
    
    async def analyze_control_health(self, context: dict) -> dict:
        """Analyze how control health impacts risk"""
        if not self.model:
            return self._get_fallback_analysis()
        
        try:
            prompt = f"""Analyze how control health impacts risk rating:
            
Context: {json.dumps(context, indent=2)}

Provide analysis and specific recommendations.

Return ONLY valid JSON:
{{
  "analysis": "Your detailed analysis here",
  "recommendations": ["rec1", "rec2", "rec3"]
}}"""
            
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            
            result = json.loads(text)
            return result
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self._get_fallback_analysis()
    
    def _get_fallback_risks(self) -> list:
        """Fallback risks when AI is not available"""
        return [
            {"name": "Data Breach", "description": "Unauthorized access to sensitive data", "category": "Cybersecurity", "inherent_score": 8.5},
            {"name": "Ransomware Attack", "description": "Malicious encryption of systems", "category": "Cybersecurity", "inherent_score": 9.0},
            {"name": "Regulatory Non-Compliance", "description": "Failure to meet regulatory requirements", "category": "Compliance", "inherent_score": 7.8},
            {"name": "Third-Party Risk", "description": "Vendor security vulnerabilities", "category": "Operational", "inherent_score": 7.2},
            {"name": "Insider Threat", "description": "Malicious or negligent employee actions", "category": "Security", "inherent_score": 6.8},
            {"name": "Business Continuity", "description": "System downtime affecting operations", "category": "Operational", "inherent_score": 8.0},
            {"name": "Financial Fraud", "description": "Fraudulent transactions", "category": "Financial", "inherent_score": 7.5},
            {"name": "Privacy Violation", "description": "Unauthorized data processing", "category": "Privacy", "inherent_score": 7.0},
            {"name": "Supply Chain Disruption", "description": "Critical supplier failure", "category": "Operational", "inherent_score": 6.5},
            {"name": "Reputational Damage", "description": "Negative publicity", "category": "Strategic", "inherent_score": 7.8}
        ]
    
    def _get_fallback_analysis(self) -> dict:
        """Fallback analysis when AI is not available"""
        return {
            "analysis": "Analysis available when Google Gemini API key is configured. Add GOOGLE_API_KEY to your .env file.",
            "recommendations": [
                "Configure Google Gemini API key for AI-powered insights",
                "Review control effectiveness regularly",
                "Monitor KRI thresholds"
            ]
        }

# Global AI service instance
ai_service = GeminiAIService()
