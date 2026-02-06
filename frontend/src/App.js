import React, { useEffect, useState } from 'react';
import '@/App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import Sidebar from '@/components/Sidebar';
import Dashboard from '@/pages/Dashboard';
import RiskIntelligence from '@/pages/RiskIntelligence';
import ControlMapping from '@/pages/ControlMapping';
import EvidenceCollection from '@/pages/EvidenceCollection';
import { Toaster } from '@/components/ui/sonner';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export const AppContext = React.createContext();

function App() {
  const [loading, setLoading] = useState(false);
  const [risks, setRisks] = useState([]);
  const [controls, setControls] = useState([]);
  const [kris, setKris] = useState([]);
  const [kcis, setKcis] = useState([]);
  const [evidence, setEvidence] = useState([]);

  useEffect(() => {
    seedDataAndFetch();
  }, []);

  const seedDataAndFetch = async () => {
    setLoading(true);
    try {
      await axios.post(`${API}/seed-data`);
      await fetchAllData();
    } catch (error) {
      console.error('Error seeding data:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchAllData = async () => {
    try {
      const [risksRes, controlsRes, krisRes, kcisRes, evidenceRes] = await Promise.all([
        axios.get(`${API}/risks`),
        axios.get(`${API}/controls`),
        axios.get(`${API}/kris`),
        axios.get(`${API}/kcis`),
        axios.get(`${API}/evidence`),
      ]);
      setRisks(risksRes.data);
      setControls(controlsRes.data);
      setKris(krisRes.data);
      setKcis(kcisRes.data);
      setEvidence(evidenceRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const contextValue = {
    risks,
    controls,
    kris,
    kcis,
    evidence,
    loading,
    refreshData: fetchAllData,
    API,
  };

  return (
    <AppContext.Provider value={contextValue}>
      <div className="App">
        <BrowserRouter>
          <div className="flex min-h-screen bg-slate-50">
            <Sidebar />
            <main className="flex-1 md:ml-64">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/risk-intelligence" element={<RiskIntelligence />} />
                <Route path="/control-mapping" element={<ControlMapping />} />
                <Route path="/evidence" element={<EvidenceCollection />} />
              </Routes>
            </main>
          </div>
        </BrowserRouter>
        <Toaster position="top-right" />
      </div>
    </AppContext.Provider>
  );
}

export default App;
