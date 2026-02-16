#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for GRC Intelligence Platform
Tests all endpoints including AI analysis functionality
"""

import requests
import json
import sys
import time
from datetime import datetime, timezone
from typing import Dict, Any, List

class GRCAPITester:
    def __init__(self, base_url: str = "https://control-mapper-1.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_base = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.failures = []
        
        # Sample data for testing
        self.test_risk_data = {
            "name": "Test Cybersecurity Risk",
            "description": "Test risk for API validation",
            "category": "Cybersecurity", 
            "inherent_risk_score": 8.0,
            "residual_risk_score": 4.0,
            "status": "Active",
            "owner": "Test CISO",
            "kris": [],
            "linked_controls": []
        }
        
        self.test_control_data = {
            "name": "Test MFA Control",
            "description": "Test control for API validation",
            "ccf_id": "CCF-TEST-001",
            "internal_policy": "POL-TEST-100",
            "control_type": "Preventive",
            "frequency": "Continuous",
            "owner": "Test IT Security",
            "health_score": 95.0,
            "status": "Effective",
            "linked_risks": [],
            "kcis": []
        }

    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test results"""
        self.tests_run += 1
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"\n{status} - {test_name}")
        if details:
            print(f"   Details: {details}")
        
        if success:
            self.tests_passed += 1
        else:
            self.failures.append({
                "test": test_name,
                "details": details
            })

    def test_health_check(self) -> bool:
        """Test basic API health"""
        try:
            response = requests.get(f"{self.api_base}/", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - Message: {data.get('message', 'No message')}"
            
            self.log_test("API Health Check", success, details)
            return success
        except Exception as e:
            self.log_test("API Health Check", False, f"Exception: {str(e)}")
            return False

    def test_seed_data(self) -> bool:
        """Test data seeding endpoint"""
        try:
            response = requests.post(f"{self.api_base}/seed-data", timeout=30)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - {data.get('message', 'No message')}"
            
            self.log_test("Seed Data", success, details)
            return success
        except Exception as e:
            self.log_test("Seed Data", False, f"Exception: {str(e)}")
            return False

    def test_get_risks(self) -> bool:
        """Test GET /api/risks endpoint"""
        try:
            response = requests.get(f"{self.api_base}/risks", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - Retrieved {len(data)} risks"
                # Verify risk structure
                if data and len(data) > 0:
                    risk = data[0]
                    required_fields = ['id', 'name', 'description', 'category', 'residual_risk_score']
                    missing_fields = [field for field in required_fields if field not in risk]
                    if missing_fields:
                        success = False
                        details += f" - Missing fields: {missing_fields}"
            
            self.log_test("GET Risks", success, details)
            return success
        except Exception as e:
            self.log_test("GET Risks", False, f"Exception: {str(e)}")
            return False

    def test_create_risk(self) -> tuple[bool, str]:
        """Test POST /api/risks endpoint"""
        try:
            response = requests.post(
                f"{self.api_base}/risks",
                json=self.test_risk_data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            risk_id = None
            
            if success:
                data = response.json()
                risk_id = data.get('id')
                details += f" - Created risk ID: {risk_id}"
            
            self.log_test("POST Risk", success, details)
            return success, risk_id
        except Exception as e:
            self.log_test("POST Risk", False, f"Exception: {str(e)}")
            return False, None

    def test_get_controls(self) -> bool:
        """Test GET /api/controls endpoint"""
        try:
            response = requests.get(f"{self.api_base}/controls", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - Retrieved {len(data)} controls"
            
            self.log_test("GET Controls", success, details)
            return success
        except Exception as e:
            self.log_test("GET Controls", False, f"Exception: {str(e)}")
            return False

    def test_create_control(self) -> tuple[bool, str]:
        """Test POST /api/controls endpoint"""
        try:
            response = requests.post(
                f"{self.api_base}/controls",
                json=self.test_control_data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            control_id = None
            
            if success:
                data = response.json()
                control_id = data.get('id')
                details += f" - Created control ID: {control_id}"
            
            self.log_test("POST Control", success, details)
            return success, control_id
        except Exception as e:
            self.log_test("POST Control", False, f"Exception: {str(e)}")
            return False, None

    def test_get_kris(self) -> bool:
        """Test GET /api/kris endpoint"""
        try:
            response = requests.get(f"{self.api_base}/kris", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - Retrieved {len(data)} KRIs"
            
            self.log_test("GET KRIs", success, details)
            return success
        except Exception as e:
            self.log_test("GET KRIs", False, f"Exception: {str(e)}")
            return False

    def test_get_kcis(self) -> bool:
        """Test GET /api/kcis endpoint"""
        try:
            response = requests.get(f"{self.api_base}/kcis", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - Retrieved {len(data)} KCIs"
            
            self.log_test("GET KCIs", success, details)
            return success
        except Exception as e:
            self.log_test("GET KCIs", False, f"Exception: {str(e)}")
            return False

    def test_get_evidence(self) -> bool:
        """Test GET /api/evidence endpoint"""
        try:
            response = requests.get(f"{self.api_base}/evidence", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f" - Retrieved {len(data)} evidence items"
            
            self.log_test("GET Evidence", success, details)
            return success
        except Exception as e:
            self.log_test("GET Evidence", False, f"Exception: {str(e)}")
            return False

    def test_ai_analysis_risk_kri_mapping(self) -> bool:
        """Test AI analysis for risk-KRI mapping"""
        try:
            analysis_request = {
                "analysis_type": "risk_kri_mapping",
                "context": {
                    "risk": {
                        "name": "Data Breach",
                        "description": "Unauthorized access to sensitive data",
                        "inherent_score": 8.5,
                        "residual_score": 4.2,
                        "category": "Cybersecurity"
                    },
                    "kris": [
                        {
                            "name": "Failed Login Attempts",
                            "current_value": 45.0,
                            "threshold": 100.0,
                            "status": "Normal",
                            "trend": "Stable"
                        }
                    ],
                    "controls": [
                        {
                            "name": "Multi-Factor Authentication", 
                            "health_score": 92.0,
                            "status": "Effective"
                        }
                    ]
                }
            }
            
            response = requests.post(
                f"{self.api_base}/ai/analyze",
                json=analysis_request,
                headers={'Content-Type': 'application/json'},
                timeout=30  # AI calls may take longer
            )
            
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                has_analysis = 'analysis' in data and data['analysis']
                has_recommendations = 'recommendations' in data
                details += f" - Analysis: {len(data.get('analysis', ''))} chars"
                details += f" - Recommendations: {len(data.get('recommendations', []))}"
                
                if not has_analysis:
                    success = False
                    details += " - Missing analysis content"
            else:
                details += f" - Response: {response.text[:100]}"
                
            self.log_test("AI Analysis - Risk KRI Mapping", success, details)
            return success
        except Exception as e:
            self.log_test("AI Analysis - Risk KRI Mapping", False, f"Exception: {str(e)}")
            return False

    def test_ai_analysis_control_health_impact(self) -> bool:
        """Test AI analysis for control health impact"""
        try:
            analysis_request = {
                "analysis_type": "control_health_impact",
                "context": {
                    "risk": {
                        "name": "Data Breach",
                        "residual_score": 4.2,
                        "inherent_score": 8.5
                    },
                    "controls": [
                        {
                            "name": "Multi-Factor Authentication",
                            "health_score": 92.0,
                            "status": "Effective",
                            "type": "Preventive"
                        }
                    ],
                    "average_control_health": 92.0,
                    "risk_reduction": 50.6
                }
            }
            
            response = requests.post(
                f"{self.api_base}/ai/analyze",
                json=analysis_request,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                has_analysis = 'analysis' in data and data['analysis']
                details += f" - Analysis: {len(data.get('analysis', ''))} chars"
                details += f" - Recommendations: {len(data.get('recommendations', []))}"
                
                if not has_analysis:
                    success = False
                    details += " - Missing analysis content"
                    
            self.log_test("AI Analysis - Control Health Impact", success, details)
            return success
        except Exception as e:
            self.log_test("AI Analysis - Control Health Impact", False, f"Exception: {str(e)}")
            return False

    def test_ai_analysis_ccf_mapping(self) -> bool:
        """Test AI analysis for CCF mapping"""
        try:
            analysis_request = {
                "analysis_type": "ccf_mapping",
                "context": {
                    "control": {
                        "name": "Multi-Factor Authentication",
                        "description": "Enforce MFA for all user accounts",
                        "ccf_id": "CCF-AC-001",
                        "internal_policy": "POL-SEC-100",
                        "type": "Preventive",
                        "frequency": "Continuous"
                    },
                    "linked_risks": [
                        {"name": "Data Breach", "category": "Cybersecurity"}
                    ],
                    "frameworks": ["ISO 27001", "SOC 2", "GDPR", "NIST CSF"]
                }
            }
            
            response = requests.post(
                f"{self.api_base}/ai/analyze",
                json=analysis_request,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                has_analysis = 'analysis' in data and data['analysis']
                details += f" - Analysis: {len(data.get('analysis', ''))} chars"
                details += f" - Recommendations: {len(data.get('recommendations', []))}"
                
                if not has_analysis:
                    success = False
                    details += " - Missing analysis content"
                    
            self.log_test("AI Analysis - CCF Mapping", success, details)
            return success
        except Exception as e:
            self.log_test("AI Analysis - CCF Mapping", False, f"Exception: {str(e)}")
            return False

    def run_all_tests(self) -> dict:
        """Run all backend API tests"""
        print("🚀 Starting GRC Intelligence Platform Backend API Tests")
        print(f"🔗 Testing against: {self.base_url}")
        print("=" * 60)
        
        # Basic connectivity tests
        if not self.test_health_check():
            print("\n💥 Critical: API health check failed. Stopping tests.")
            return self.get_results()
        
        # Seed data first
        if not self.test_seed_data():
            print("\n⚠️  Warning: Data seeding failed, but continuing with tests...")
        
        # Test all CRUD endpoints
        self.test_get_risks()
        self.test_create_risk()
        self.test_get_controls()
        self.test_create_control()
        self.test_get_kris()
        self.test_get_kcis()
        self.test_get_evidence()
        
        # Test AI analysis features (these may be slower)
        print("\n🤖 Testing AI Analysis Features...")
        print("⏳ Note: AI analysis tests may take 10-30 seconds each...")
        
        self.test_ai_analysis_risk_kri_mapping()
        self.test_ai_analysis_control_health_impact()
        self.test_ai_analysis_ccf_mapping()
        
        return self.get_results()

    def get_results(self) -> dict:
        """Get test results summary"""
        success_rate = (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0
        
        return {
            "tests_run": self.tests_run,
            "tests_passed": self.tests_passed,
            "tests_failed": self.tests_run - self.tests_passed,
            "success_rate": round(success_rate, 1),
            "failures": self.failures
        }

    def print_summary(self):
        """Print test results summary"""
        results = self.get_results()
        
        print("\n" + "=" * 60)
        print("📊 BACKEND API TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {results['tests_run']}")
        print(f"Passed: {results['tests_passed']} ✅")
        print(f"Failed: {results['tests_failed']} ❌")
        print(f"Success Rate: {results['success_rate']}%")
        
        if results['failures']:
            print("\n🔍 FAILED TESTS:")
            for failure in results['failures']:
                print(f"  ❌ {failure['test']}: {failure['details']}")
        
        print("\n" + "=" * 60)
        
        if results['success_rate'] >= 80:
            print("🎉 Backend API tests mostly successful!")
        elif results['success_rate'] >= 60:
            print("⚠️  Backend API has some issues that need attention.")
        else:
            print("🚨 Backend API has significant issues requiring immediate attention.")

def main():
    """Main test execution"""
    tester = GRCAPITester()
    results = tester.run_all_tests()
    tester.print_summary()
    
    # Return appropriate exit code
    return 0 if results['success_rate'] >= 80 else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)