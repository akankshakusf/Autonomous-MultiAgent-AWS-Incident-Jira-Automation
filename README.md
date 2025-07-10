# Autonomous JIRA Incident Creation System for AWS

### Architecture

<img src="https://github.com/akankshakusf/Autonomous-MultiAgent-AWS-Incident-Jira-Automation/blob/main/images/arch%202.png" width="100%" />

## 🚀 Overview

This project shows how AI-powered multi-agent systems can revolutionize cloud incident response. Built using Amazon Bedrock (Claude & Nova), OpenAI embeddings, and advanced monitoring with AWS CloudWatch and CloudTrail, LangSmith used for debugging this solution detects, diagnoses, and resolves incidents—eliminating manual JIRA ticket creation and dramatically reducing response times.

---

## 🧠 Key Features

- **Continuous AWS Monitoring:**  
  Detects issues across data pipelines, compute resources, storage, and access boundaries in real time.

- **RAG-Powered Diagnosis:**  
  Finds solutions using a vector store of previous incidents; escalates to web search for novel problems.

- **Autonomous Ticket Creation:**  
  Generates detailed JIRA tickets with incident context, root cause, and actionable remediation steps. Later, sends a Push Notification to Team.

- **Multi-Agent Architecture:**  
  - **Supervisor Agent:** Orchestrates the workflow and manages agent handoff state.
  - **Monitoring Agent:** Watches AWS logs and resources, detects anomalies.
  - **Diagnosis Agent:** Uses RAG (vector DB + Tavily web search) for recommended fixes.
  - **Resolution Agent:** Creates JIRA tickets for each incident, sends a Push Notification to Team.

- **Self-Learning Memory:**  
  The system’s knowledge base grows with every new incident and solution.

---

## 🏢 How Teams Can Use This System

This system is built for real-world, collaborative cloud operations. At the **American Red Cross**, our team uses it to monitor critical AWS services, automate incident response, and reduce operational overhead:

- **24/7 Monitoring:** The system continuously tracks data pipelines, compute resources, storage, and access patterns, catching incidents the moment they occur.
- **Automated Triage & Context:** Instead of sifting through scattered logs and alerts, engineers receive actionable JIRA tickets for every significant event—complete with root cause, context, and step-by-step remediation.
- **Self-Improving Knowledge Base:** Each new incident handled expands the system’s internal memory, enabling even faster, more accurate responses for future issues.
- **Seamless Collaboration:** Support, DevOps, and security teams are notified instantly and can trust that every ticket includes the right context and remediation plan—streamlining handoffs and reducing time-to-resolution.
- **Reduced Alert Fatigue:** Teams focus only on actionable, high-priority incidents with recommended fixes—helping them stay proactive, not reactive.

**How to Start Using It in Your Team:**
- Deploy the system to monitor the AWS resources your team relies on.
- Integrate the JIRA ticketing automation into your support or DevOps workflow.
- Let the agents handle detection, diagnosis, and documentation—your engineers focus on solutions and improvements.
- As the memory database grows, incident response becomes faster, more consistent, and more intelligent.

**At the American Red Cross, this solution has transformed the way our technical teams respond to incidents.  
Manual triage is now a thing of the past. We’ve cut response times, increased transparency, and enabled true collaboration across operations, support, and security.**

---

## 💻 Tech Stack

- **Python**
- **Amazon Bedrock (Claude, Nova)**
- **OpenAI Embeddings**
- **LangChain**
- **AWS CloudWatch & CloudTrail**
- **JIRA API**
- **Tavily (Web Search API)**
- **LangSmith**




