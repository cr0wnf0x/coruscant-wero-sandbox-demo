# mcp_fraud_server.py
from mcp.server.fastmcp import FastMCP

# Create a simple MCP server
mcp = FastMCP("CCB Fraud Oracle")

# A dummy database of flagged IBANs
FLAGGED_IBANS = {
    "DE123456789012345678": "High Risk - Suspicious Activity",
    "DE999999999999999999": "Sanctioned Entity"
}

@mcp.tool()
def check_iban_fraud_status(iban: str) -> str:
    """Checks the Coruscant Central Bank fraud database for a given IBAN."""
    if iban in FLAGGED_IBANS:
        return f"REJECT: IBAN {iban} is flagged. Reason: {FLAGGED_IBANS[iban]}"
    return f"APPROVE: IBAN {iban} is clean."

if __name__ == "__main__":
    # In a real-world scenario, we run this as a persistent SSE service.
    # This allows multiple clients to connect to the same Fraud Oracle.
    mcp.run(transport='sse')
