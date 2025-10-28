## What is MCP?
MCP is a standard for connecting AI applications to external systems which are local or public. The goal of MCP is to expose certain endpoints to AI clients like Gemini, Claude, and ChatGPT so that they can call them effectively.

## MCP has two layers
- Data Layer
    - RPC (Remote Procedure Call)
    - Good communication prtotocol for switching between 
    - JSON-RPC 2.0: Establishes message structure and semantics
        - Requests
        - Responses
        - Notifications
- Transport Layer
    - Stdio transport
        - Local Communciation
            - Reduce Network Load
    - Streamable HTTP Transport
        - HTTP Post for client-to-server
        - Server-sent events

## Practical Implementation
MCP Servers can be hosted on serverless environments in addition to container like docker.

### FastMCP
Python framework for building MCP applciations. Can be hosted on [Prefect](https://www.prefect.io/pricing?plan=start)

## Key Terminology
- Primitives
    - Tools: Function that can be called by AI
    - Resources: Data sources that provide contextual info to AI applications
    - Prompts: Templates that allow for interaction
- Primitives can be exposed both ways
    - Clients usually expose 
        - sampling/complete
        - elicitation/request

## References
1) https://build.microsoft.com/en-US/sessions/DEM517
2)  https://modelcontextprotocol.io/docs/getting-started/intro
3) https://www.jsonrpc.org/specification
4) https://medium.com/@dan.avila7/why-model-context-protocol-uses-json-rpc-64d466112338
5) https://www.geeksforgeeks.org/operating-systems/remote-procedure-call-rpc-in-operating-system/



