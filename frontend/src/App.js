import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Area,
  AreaChart,
} from "recharts";

const glass = {
  background: "rgba(255,255,255,0.08)",
  backdropFilter: "blur(20px)",
  border: "1px solid rgba(255,255,255,0.15)",
  borderRadius: 20,
  padding: 25,
  boxShadow: "0 20px 60px rgba(0,0,0,0.4)",
};

export default function App() {
  const [page, setPage] = useState("dashboard");
  const [collapsed, setCollapsed] = useState(false);
  const [risk, setRisk] = useState(35);
  const [health, setHealth] = useState("HEALTHY");

  // 🔥 Realistic Dynamic Risk Engine
  useEffect(() => {
    const interval = setInterval(() => {
      setRisk((prev) => {
        let next = prev + (Math.random() * 20 - 10);
        next = Math.max(5, Math.min(95, Math.floor(next)));

        if (next < 40) setHealth("HEALTHY");
        else if (next < 75) setHealth("DEGRADED");
        else setHealth("CRITICAL");

        return next;
      });
    }, 4000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        background:
          "radial-gradient(circle at 20% 20%, #1e3a8a, transparent 40%), radial-gradient(circle at 80% 80%, #7c3aed, transparent 40%), #0f172a",
        color: "white",
        fontFamily: "Inter, sans-serif",
      }}
    >
      {/* Sidebar */}
      <motion.div
        animate={{ width: collapsed ? 80 : 240 }}
        transition={{ duration: 0.3 }}
        style={{
          background: "rgba(255,255,255,0.05)",
          backdropFilter: "blur(15px)",
          padding: 20,
          display: "flex",
          flexDirection: "column",
          gap: 25,
        }}
      >
        <button
          onClick={() => setCollapsed(!collapsed)}
          style={{ background: "none", color: "white", border: "none" }}
        >
          {collapsed ? ">>" : "<<"}
        </button>

        <Nav label="dashboard" setPage={setPage} collapsed={collapsed} />
        <Nav label="monitoring" setPage={setPage} collapsed={collapsed} />
        <Nav label="ai insights" setPage={setPage} collapsed={collapsed} />
        <Nav label="api" setPage={setPage} collapsed={collapsed} />
      </motion.div>

      {/* Main */}
      <div style={{ flex: 1, padding: 40 }}>
        {/* Top Status */}
        <motion.div
          layout
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: 40,
          }}
        >
          <h1>AI Predictive Failure Intelligence</h1>

          <motion.div
            key={health}
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 10,
              padding: "8px 20px",
              borderRadius: 30,
              background:
                health === "HEALTHY"
                  ? "rgba(34,197,94,0.2)"
                  : health === "DEGRADED"
                  ? "rgba(234,179,8,0.2)"
                  : "rgba(239,68,68,0.2)",
            }}
          >
            <div
              style={{
                width: 12,
                height: 12,
                borderRadius: "50%",
                background:
                  health === "HEALTHY"
                    ? "#22c55e"
                    : health === "DEGRADED"
                    ? "#eab308"
                    : "#ef4444",
                boxShadow:
                  health === "HEALTHY"
                    ? "0 0 15px #22c55e"
                    : health === "DEGRADED"
                    ? "0 0 15px #eab308"
                    : "0 0 15px #ef4444",
              }}
            />
            {health}
          </motion.div>
        </motion.div>

        <AnimatePresence mode="wait">
          {page === "dashboard" && (
            <Dashboard risk={risk} health={health} />
          )}
          {page === "monitoring" && (
            <Monitoring risk={risk} health={health} />
          )}
          {page === "ai insights" && <Insights risk={risk} />}
          {page === "api" && <API />}
        </AnimatePresence>
      </div>
    </div>
  );
}

function Nav({ label, setPage, collapsed }) {
  return (
    <motion.div
      whileHover={{ scale: 1.05 }}
      onClick={() => setPage(label)}
      style={{
        cursor: "pointer",
        padding: 12,
        borderRadius: 12,
        background: "rgba(255,255,255,0.08)",
        textTransform: "capitalize",
      }}
    >
      {collapsed ? label[0] : label}
    </motion.div>
  );
}

/* ================= DASHBOARD ================= */

function Dashboard({ risk, health }) {
  const [prediction, setPrediction] = useState("");

  useEffect(() => {
    if (health === "HEALTHY")
      setPrediction("System stable. No anomaly patterns detected.");
    else if (health === "DEGRADED")
      setPrediction("Latency spike trend emerging.");
    else
      setPrediction(
        "High probability cascading failure predicted."
      );
  }, [health]);

  const data = Array.from({ length: 10 }).map((_, i) => ({
    time: `T-${10 - i}`,
    value: Math.max(5, Math.min(95, risk + (Math.random() * 15 - 8))),
  }));

  return (
    <motion.div
      key="dash"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      style={{ display: "flex", flexDirection: "column", gap: 30 }}
    >
      <motion.div style={glass}>
        <h2>Risk Trend Analysis</h2>
        <div style={{ height: 250, marginTop: 20 }}>
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#444" />
              <XAxis dataKey="time" stroke="#aaa" />
              <YAxis stroke="#aaa" />
              <Tooltip />
              <Area
                type="monotone"
                dataKey="value"
                stroke="#7c3aed"
                fill="#7c3aed"
                fillOpacity={0.3}
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </motion.div>

      <motion.div style={glass}>
        <h2>AI Prediction Engine</h2>
        <p style={{ marginTop: 15 }}>{prediction}</p>
      </motion.div>
    </motion.div>
  );
}

/* ================= MONITORING ================= */

function Monitoring({ risk }) {
  const [logs, setLogs] = useState([]);
  const [countdown, setCountdown] = useState(180);

  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    const logInterval = setInterval(() => {
      const messages = [
        "[INFO] Monitoring CPU load",
        "[WARN] Latency deviation detected",
        "[AI] Risk recalculated",
        "[ALERT] Correlated anomaly cluster formed",
      ];
      const random =
        messages[Math.floor(Math.random() * messages.length)];
      setLogs((prev) => [...prev.slice(-6), random]);
    }, 3000);

    return () => clearInterval(logInterval);
  }, []);

  return (
    <motion.div
      key="mon"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      style={{ display: "flex", flexDirection: "column", gap: 30 }}
    >
      <motion.div style={glass}>
        <h2>Incident Cluster</h2>
        <p>Cascade Probability: {risk}%</p>
        <p>
          Predicted Degradation In:{" "}
          {Math.floor(countdown / 60)}:
          {(countdown % 60).toString().padStart(2, "0")}
        </p>
      </motion.div>

      <motion.div style={{ ...glass, fontFamily: "monospace" }}>
        <h3>Live Logs</h3>
        {logs.map((log, i) => (
          <motion.p key={i} initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
            {log}
          </motion.p>
        ))}
      </motion.div>
    </motion.div>
  );
}

/* ================= INSIGHTS ================= */

function Insights({ risk }) {
  const features = [
    { name: "CPU Usage", value: 85 },
    { name: "Latency", value: 70 },
    { name: "Error Rate", value: 78 },
    { name: "Memory Load", value: 60 },
  ];

  return (
    <motion.div
      key="ins"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      style={{ display: "flex", flexDirection: "column", gap: 30 }}
    >
      <motion.div style={glass}>
        <h2>Model Architecture</h2>
        <p>Hybrid LSTM + Correlation Engine</p>
      </motion.div>

      <motion.div style={glass}>
        <h2>Feature Importance</h2>

        {features.map((feature, index) => (
          <div key={index} style={{ marginTop: 20 }}>
            <p>{feature.name}</p>
            <div
              style={{
                height: 12,
                background: "rgba(255,255,255,0.1)",
                borderRadius: 10,
                overflow: "hidden",
                marginTop: 5,
              }}
            >
              <motion.div
                initial={{ width: 0 }}
                animate={{ width: `${feature.value}%` }}
                transition={{ duration: 1 }}
                style={{
                  height: "100%",
                  background: "#7c3aed",
                }}
              />
            </div>
          </div>
        ))}
      </motion.div>

      <motion.div style={glass}>
        <h2>Prediction Confidence</h2>
        <h1>{Math.min(99, risk + 10)}%</h1>
      </motion.div>
    </motion.div>
  );
}

/* ================= API ================= */

function API() {
  return (
    <motion.div
      key="api"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      style={{ display: "flex", flexDirection: "column", gap: 30 }}
    >
      <motion.div style={glass}>
        <h2>API Key Integration</h2>
        <input
          placeholder="Enter API Key"
          style={{
            marginTop: 20,
            padding: 12,
            borderRadius: 12,
            border: "none",
            width: "100%",
          }}
        />
      </motion.div>
    </motion.div>
  );
}