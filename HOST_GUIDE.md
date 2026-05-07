# 🎭 Host & Speaker Guide: Coruscant Central Bank (CCB)

> [!TIP]
> **Use the Interactive Portal!**
> Open **[ccb_portal.html](./ccb_portal.html)** and set the toggle to **"Imperial Officer"** for a sleek, themed dashboard to use during your presentation.

## 🏗️ Pre-Workshop Setup 

1. **Clear the session history (CRITICAL):**
   ```bash
   gemini /clear
   ```
2. **Re-initialize the project:**
   ```bash
   gemini /init
   ```
3. **Start the Mock Services (Run in two separate terminal tabs):**
   ```bash
   # Tab 1: The API Gateway
   python3 mock_gateway.py
   
   # Tab 2: The MCP Fraud Oracle
   python3 mcp_fraud_server.py
   ```
4. **Register the MCP server with Gemini CLI:**
   ```bash
   gemini mcp add --transport sse fraud-oracle http://localhost:8000/sse
   ```

---

## 🧭 Live Demo Script & Narrative Flow

### 🔹 Module I: The "Central Hub" (/init & /clear)
* **Narrative:** "Welcome to the Coruscant Central Bank. We start with `/clear` to ensure no old data interferes, and `/init` to map our local Wero templates safely."

### 🔹 Module II: Custom Commands (The Hyperdrive)
* **Narrative:** "With `@` we pull in our official ISO 20022 templates, and with `!` we trigger our local Coruscant validators before hitting the API."

### 🔹 Module III: Persistence (/resume)
* **Narrative:** "Communication disrupted? `/resume` picks up the transaction thread instantly."

### 🔹 Module IV: The Logistics Pipe (-p)
* **Narrative:** "We pipe failure logs directly to Gemini to translate cryptic error codes like 'RR04' into plain German."

### 🔹 Module V: Enterprise Tooling (MCP)
* **Action:** Run a query that forces Gemini to check the MCP fraud server.
* **Narrative:** "Static templates are great, but banks need real-time data. We are running an MCP server locally. Watch what happens when I ask Gemini to verify a suspicious IBAN. It autonomously decides to query the Fraud Oracle database."
* **The "Miro Board" Tie-In:** "Today we use a local Python script for our database, but this exact same MCP standard is what you use to connect Gemini to **Google Docs** for automated compliance reports, or **GKE-MCP** to debug our Kubernetes clusters."

---

## 🏆 The "Flipped Goal" (DIY Segment)
Help teams create a **Custom Persona** ("Senior Imperial Auditor") and generate a **Mermaid.js** diagram mapping the flow from the Client -> Validator -> MCP Oracle -> Gateway.
