
import { useEffect, useState } from "react";

type HealthResponse = {
  status: string;
  application: string;
  version: string;
};

export default function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(
      `${import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000"}/api/health`
    )
      .then((response) => {
        if (!response.ok) {
          throw new Error("Backend memberikan respons error.");
        }

        return response.json();
      })
      .then((data: HealthResponse) => setHealth(data))
      .catch(() => {
        setError("Backend belum terhubung.");
      });
  }, []);

  return (
    <main>
      <aside className="sidebar">
        <h2>NexaERP AI</h2>
        <p>Business Operations</p>

        <nav>
          <div>Dashboard</div>
          <div>Inventory</div>
          <div>Procurement</div>
          <div>Suppliers</div>
          <div>PPIC</div>
          <div>AI Assistant</div>
        </nav>
      </aside>

      <section className="content">
        <header>
          <div>
            <p className="eyebrow">BUSINESS OVERVIEW</p>
            <h1>Dashboard</h1>
          </div>
          <span className="status">
            {health ? "API Connected" : "Checking API..."}
          </span>
        </header>

        <div className="welcome">
          <p className="eyebrow">ERP WORKSPACE</p>
          <h2>Selamat datang di NexaERP AI</h2>
          <p>
            Kelola inventory, procurement, supplier, dan perencanaan
            produksi dalam satu platform.
          </p>
        </div>

        <div className="cards">
          <article>
            <p>Total Items</p>
            <h2>—</h2>
            <span>Inventory</span>
          </article>

          <article>
            <p>Active Purchase Orders</p>
            <h2>—</h2>
            <span>Procurement</span>
          </article>

          <article>
            <p>Production Orders</p>
            <h2>—</h2>
            <span>PPIC</span>
          </article>
        </div>

        <section className="assistant">
          <h2>AI Assistant</h2>
          <p>
            Tanya tentang stok, PO terlambat, dan kebutuhan material.
          </p>
          <div className="assistant-input">
            <span>AI Assistant akan tersedia pada tahap berikutnya.</span>
            <button disabled>Ask AI</button>
          </div>
        </section>

        {error && <p className="error">{error}</p>}
      </section>
    </main>
  );
}
