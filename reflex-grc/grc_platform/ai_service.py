"""Google Gemini AI service for GRC analysis"""
import google.generativeai as genai
import os
import json
import warnings
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=FutureWarning)

class GeminiAIService:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY", "")
        if api_key and api_key != "your_gemini_api_key_here":
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
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
    
    def analyze_compliance_gaps(self, framework_name: str, framework_controls: list, unified_controls: list, policies: list) -> dict:
        """AI-powered compliance gap analysis for a specific framework"""
        if not self.model:
            return self._get_fallback_gap_analysis(framework_name)
        
        try:
            # Build context about current compliance posture
            mapped_controls = []
            for uc in unified_controls:
                for mapping in uc.get("mapped_framework_controls", []):
                    if mapping.get("framework") == framework_name:
                        mapped_controls.append({
                            "ccf_id": uc.get("ccf_id"),
                            "name": uc.get("name"),
                            "status": uc.get("status"),
                            "framework_control_id": mapping.get("control_id"),
                            "framework_control_name": mapping.get("control_name")
                        })
            
            policy_names = [p.get("name") for p in policies]
            
            prompt = f"""You are a senior GRC compliance auditor. Perform a comprehensive compliance gap analysis for the "{framework_name}" framework.

CURRENT STATE:
- Framework: {framework_name}
- Mapped unified controls ({len(mapped_controls)} total): {json.dumps(mapped_controls[:15], indent=1)}
- Active policies: {json.dumps(policy_names, indent=1)}

TASK: Analyze the organization's compliance posture against {framework_name} and identify gaps.

Return ONLY valid JSON with this exact structure:
{{
  "overall_score": 72,
  "maturity_level": "Developing",
  "summary": "Brief 2-sentence executive summary of compliance posture",
  "strengths": [
    {{"area": "Area name", "detail": "What is strong and why"}},
    {{"area": "Area name", "detail": "What is strong and why"}}
  ],
  "critical_gaps": [
    {{"gap": "Gap title", "severity": "Critical", "detail": "What is missing", "recommendation": "How to fix it"}},
    {{"gap": "Gap title", "severity": "High", "detail": "What is missing", "recommendation": "How to fix it"}}
  ],
  "improvements": [
    {{"area": "Area name", "current_state": "Current status", "target_state": "Where it should be", "effort": "Low/Medium/High"}}
  ],
  "quick_wins": [
    "Quick actionable item 1",
    "Quick actionable item 2"
  ],
  "roadmap": [
    {{"phase": "Phase 1 (0-30 days)", "actions": ["action1", "action2"]}},
    {{"phase": "Phase 2 (30-90 days)", "actions": ["action1", "action2"]}},
    {{"phase": "Phase 3 (90-180 days)", "actions": ["action1", "action2"]}}
  ]
}}

Ensure overall_score is 0-100. Be specific and actionable. Return ONLY the JSON."""

            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            
            result = json.loads(text)
            return result
            
        except Exception as e:
            print(f"Gemini gap analysis error: {e}")
            return self._get_fallback_gap_analysis(framework_name)
    
    def _get_fallback_gap_analysis(self, framework_name: str) -> dict:
        """Fallback gap analysis when AI is unavailable"""
        return {
            "overall_score": 65,
            "maturity_level": "Developing",
            "summary": f"Preliminary gap analysis for {framework_name}. Configure Gemini API key for AI-powered deep analysis.",
            "strengths": [
                {"area": "Access Control", "detail": "Basic access control policies are in place"},
                {"area": "Incident Response", "detail": "Incident response procedures documented"}
            ],
            "critical_gaps": [
                {"gap": "Risk Assessment Process", "severity": "Critical", "detail": "No formal risk assessment methodology", "recommendation": "Implement a structured risk assessment framework"},
                {"gap": "Third-Party Management", "severity": "High", "detail": "Vendor risk management is informal", "recommendation": "Establish vendor risk assessment program"},
                {"gap": "Business Continuity", "severity": "High", "detail": "BCP/DR plans not tested recently", "recommendation": "Schedule quarterly BCP/DR testing"}
            ],
            "improvements": [
                {"area": "Security Awareness", "current_state": "Annual training only", "target_state": "Continuous awareness program", "effort": "Medium"},
                {"area": "Monitoring", "current_state": "Basic log collection", "target_state": "SIEM with real-time alerting", "effort": "High"}
            ],
            "quick_wins": [
                "Update all policy documents to current year",
                "Enable MFA for all administrative accounts",
                "Document data classification scheme"
            ],
            "roadmap": [
                {"phase": "Phase 1 (0-30 days)", "actions": ["Complete policy review", "Enable MFA everywhere"]},
                {"phase": "Phase 2 (30-90 days)", "actions": ["Implement vendor risk program", "Deploy SIEM solution"]},
                {"phase": "Phase 3 (90-180 days)", "actions": ["Conduct full risk assessment", "Achieve certification readiness"]}
            ]
        }

# Global AI service instance
ai_service = GeminiAIService()
