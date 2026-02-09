import React, { useEffect, useState } from 'react';
import '@/App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import Sidebar from '@/components/Sidebar';
import Dashboard from '@/pages/Dashboard';
import FrameworkManagement from '@/pages/FrameworkManagement';
import ControlMapping from '@/pages/ControlMapping';
import PolicyManagement from '@/pages/PolicyManagement';
import ControlTesting from '@/pages/ControlTesting';
import IssueManagement from '@/pages/IssueManagement';
import RiskManagement from '@/pages/RiskManagement';
import KRIManagement from '@/pages/KRIManagement';
import KCIManagement from '@/pages/KCIManagement';
import { Toaster } from '@/components/ui/sonner';
import { toast } from 'sonner';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export const AppContext = React.createContext();

function App() {
  const [loading, setLoading] = useState(false);
  const [dataLoaded, setDataLoaded] = useState(false);
  
  // State for all entities
  const [frameworks, setFrameworks] = useState([]);
  const [frameworkControls, setFrameworkControls] = useState([]);
  const [unifiedControls, setUnifiedControls] = useState([]);
  const [policies, setPolicies] = useState([]);
  const [controlTests, setControlTests] = useState([]);
  const [evidence, setEvidence] = useState([]);
  const [issues, setIssues] = useState([]);
  const [risks, setRisks] = useState([]);
  const [kris, setKris] = useState([]);
  const [kcis, setKcis] = useState([]);

  useEffect(() => {
    initializeApp();
  }, []);

  const initializeApp = async () => {
    setLoading(true);
    try {
      // Seed production data on first load
      await axios.post(`${API}/seed-production-data`);
      toast.success('Platform initialized successfully');
      await fetchAllData();
      setDataLoaded(true);
    } catch (error) {
      console.error('Error initializing app:', error);
      toast.error('Failed to initialize platform');
    } finally {
      setLoading(false);
    }
  };

  const fetchAllData = async () => {
    try {
      const [fwRes, ucRes, polRes, testRes, evRes, issueRes, riskRes, kriRes, kciRes] = await Promise.all([
        axios.get(`${API}/frameworks`),
        axios.get(`${API}/unified-controls`),
        axios.get(`${API}/policies`),
        axios.get(`${API}/control-tests`),
        axios.get(`${API}/evidence`),
        axios.get(`${API}/issues`),
        axios.get(`${API}/risks`),
        axios.get(`${API}/kris`),
        axios.get(`${API}/kcis`),
      ]);
      
      setFrameworks(fwRes.data);
      setUnifiedControls(ucRes.data);
      setPolicies(polRes.data);
      setControlTests(testRes.data);
      setEvidence(evRes.data);
      setIssues(issueRes.data);
      setRisks(riskRes.data);
      setKris(kriRes.data);
      setKcis(kciRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
      toast.error('Failed to fetch data');
    }
  };

  const contextValue = {
    frameworks,
    setFrameworks,
    frameworkControls,
    setFrameworkControls,
    unifiedControls,
    setUnifiedControls,
    policies,
    setPolicies,
    controlTests,
    setControlTests,
    evidence,
    setEvidence,
    issues,
    setIssues,
    risks,
    setRisks,
    kris,
    setKris,
    kcis,
    setKcis,
    loading,
    dataLoaded,
    refreshData: fetchAllData,
    API,
  };

  if (loading && !dataLoaded) {
    return (
      <div className="flex items-center justify-center h-screen bg-slate-50">
        <div className="text-center">
          <div className="h-16 w-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-lg text-slate-700 font-medium">Initializing GRC Platform...</p>
          <p className="text-sm text-slate-500 mt-2">Loading frameworks and controls</p>
        </div>
      </div>
    );
  }

  return (
    <AppContext.Provider value={contextValue}>
      <div className="App">
        <BrowserRouter>
          <div className="flex min-h-screen bg-slate-50">
            <Sidebar />
            <main className="flex-1 md:ml-64">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/frameworks" element={<FrameworkManagement />} />
                <Route path="/control-mapping" element={<ControlMapping />} />
                <Route path="/policies" element={<PolicyManagement />} />
                <Route path="/control-testing" element={<ControlTesting />} />
                <Route path="/issues" element={<IssueManagement />} />
                <Route path="/risks" element={<RiskManagement />} />
                <Route path="/kris" element={<KRIManagement />} />
                <Route path="/kcis" element={<KCIManagement />} />
              </Routes>
            </main>
          </div>
        </BrowserRouter>
        <Toaster position="top-right" richColors />
      </div>
    </AppContext.Provider>
  );
}

export default App;
