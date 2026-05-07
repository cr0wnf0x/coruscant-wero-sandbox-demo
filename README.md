# 🏛️ Coruscant Central Bank (CCB) - Wero API Sandbox

Welcome to the **Coruscant Central Bank (CCB)** developer sandbox! 

## 🚀 The Strategic Command Center (Interactive Guide)

For the most immersive experience, we have created a dedicated **Interactive Portal**. This is your central hub for the workshop, designed to look and feel like an Imperial Bank Terminal.

![CCB Portal Preview](./portal_preview.svg)

### Why use the Portal?
*   **Dual-Track Navigation:** Toggle between **"Local Operative"** (for solo setup) and **"Imperial Officer"** (for hosted workshops).
*   **Tactical Intelligence:** Click **"Show Intelligence Reports"** to reveal deep-dives into how each Gemini CLI command works under the hood.
*   **One-Click Deployment:** Copy commands directly to your clipboard with themed "Terminal" blocks.
*   **Live Narrative:** Follow the story of the Wero implementation through "Mission Directives" and "Grand Admiral Briefings."

👉 **[Launch the CCB Portal (ccb_portal.html)](./ccb_portal.html)**

---

## 📁 Repository Structure

* **`/templates`**: XML payloads (`pacs_008_template.xml`, `pain_001_template.xml`).
* **`/logs`**: Dummy clearing logs for log-triage automation.
* **`mock_gateway.py`**: A local Python Flask server (The CCB Central Clearing Hub).
* **`validate_iso.py`**: A local script to validate payload structures.
* **`mcp_fraud_server.py`**: A local MCP server acting as our real-time Fraud Oracle.
* **`HOST_GUIDE.md`**: Narrative flow and setup instructions for the moderator.
* **`PARTICIPANT_GUIDE.md`**: Step-by-step lab instructions for developers.

---

## 🚀 Workshop Modules Overview

### 1️⃣ Project Bootstrap
Initialize the workspace to let Gemini map our local environment and banking templates without uploading sensitive files to the cloud.

### 2️⃣ Custom Commands (The Hyperdrive)
Build custom commands (`/wero-send`) to pass dynamic arguments, inject local files (`@`), and execute Python validation scripts directly from the prompt (`!`).

### 3️⃣ Context & Memory (`/resume`)
Learn how to use `/resume` to pick up exactly where you left off in complex debugging scenarios after an interruption.

### 4️⃣ Power Pipelines (Non-Interactive)
Pipe (`|`) raw clearing logs directly into Gemini to instantly translate cryptic ISO error codes into actionable fixes.

### 5️⃣ Live Oracles (Model Context Protocol - MCP)
Static files aren't enough for enterprise banking. Connect Gemini to a live, local database (our Fraud Oracle) using MCP to verify if an IBAN is sanctioned before generating a payment payload.

---

## 🎯 The Finale: Flipped Goals & Extensions

Take control of the security perimeter:
1.  **Personas:** Configure Gemini to act as a *Strict Imperial Compliance Auditor*.
2.  **Architecture Flow:** Generate a **Mermaid.js** diagram of the transaction flow.
3.  **Enterprise MCPs:** Discuss extending our local MCP logic to **Google Docs** (for automated audit reporting) and **GKE-MCP** (for querying Kubernetes pod states).

> *"Processing your SEPA transfers in less than 12 parsecs."*
