# 🚀 Lab Guide: Coruscant Central Bank (CCB) Sandbox

Welcome, Developer. Today, we test our new Wero Instant Payment gateway and integrate real-time fraud detection.

---

## 🛠️ Step 0: Initializing Your Terminal

1. **Clone the central sandbox:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-org>/coruscant-wero-sandbox.git
   cd coruscant-wero-sandbox
   ```
2. **Reset your session & install dependencies:**
   ```bash
   gemini /clear
   pip install flask lxml requests mcp
   ```
3. **Start the Core Services (Run these in two separate background tabs):**
   ```bash
   python3 mock_gateway.py
   python3 mcp_fraud_server.py
   ```
4. **Map the CCB repository:**
   ```bash
   gemini /init
   ```

---

## 📦 Module 1: Understanding the Context
```bash
gemini "Identify the mandatory fields in @(templates/pacs_008_template.xml) for a CCB transfer."
```

---

## 🧪 Module 2: The Hyperdrive (Custom Commands)
Automate the generation and validation of a payment.
```bash
gemini "Create a custom command '/wero-send' that takes {{amount}} and {{iban}}, injects them into @(templates/pacs_008_template.xml), and runs !(python3 validate_iso.py)."
```
Execute a test:
```bash
gemini /wero-send 500.00 DE123456789012345678
```

---

## ⏳ Module 3: Context & Resume
```bash
gemini "How do I add a 'Settlement Priority' to this XML?"
gemini /resume "Based on that, generate the snippet for 'High Priority'."
```

---

## 🤖 Module 4: Log Triage (Non-Interactive)
```bash
cat logs/clearing.log | gemini -p "Identify any 'MS03' errors in these logs and provide a resolution."
```

---

## 🛡️ Module 5: Live Database Queries (MCP)
LLMs don't know your live database state. We use the **Model Context Protocol (MCP)** to give Gemini secure, real-time tool access.

Ask Gemini to check an IBAN against the local Fraud Oracle we started in Step 0:
```bash
gemini "Check the fraud status for IBAN DE999999999999999999 and tell me if we should block the payment."
```
*Notice how Gemini recognizes it lacks this knowledge, calls the MCP tool automatically, and returns the strict Coruscant Bank policy decision.*

---

## 🏆 DIY Challenge: Flipped Goals
1. **Set a Persona:** `gemini "Set your persona to act as a strict Imperial Compliance Auditor."`
2. **Audit:** `gemini "Audit our pacs.008 template for any vulnerabilities."`
3. **Visualize & Extend:** `gemini "Generate a Mermaid.js flowchart showing the payment path."` Think about how you would swap our local Fraud Oracle for a **GKE-MCP** connection to check pod health!
