# AI Study Platform

A full-stack study productivity platform with a stateless event-driven focus timer, analytics engine, and RAG-powered AI tutor.

## Features

### Stateless Focus Timer
- Event-sourced timer (start / pause / resume / stop)
- State reconstructed from persisted events
- Survives refresh, device switch, and server restarts
- Multi-device safe

### Notes and Subjects
- Subject-based organization
- Rich note creation
- Real-time sync
- Automatic embedding generation for AI retrieval

### Analytics Engine
- Aggregation-based metrics service
- Daily, weekly, and monthly study summaries
- Subject distribution
- 14-day trend analysis
- Streak tracking

### AI Tutor (RAG Architecture)
- Note chunking
- Embedding generation
- Vector similarity search
- Context retrieval
- LLM response generation

## Architecture Overview

The system follows a modular container-based architecture:

Frontend (Next.js) -> Backend API (Node.js) -> Supabase (PostgreSQL + pgvector) -> External LLM (OpenAI / Groq)

### Key Architectural Decisions
- Stateless timer using event sourcing
- Server-side RAG retrieval
- Clear separation of frontend modules and backend services
- Embedding-based contextual tutoring
- Horizontal scaling-safe design

## Tech Stack

**Frontend**
- Next.js, React, Redux, Recharts, Framer Motion

**Backend**
- Node.js, NextAuth (JWT + OAuth), Supabase

**Database**
- PostgreSQL, pgvector (vector storage)

**AI**
- OpenAI / Groq LLM, Embedding model, Retrieval pipeline

**Deployment**
- Vercel (Frontend), Render (Backend)

## AI Tutor Pipeline (RAG)

1. User submits a question
2. Query embedding is generated
3. Vector similarity search runs against note embeddings
4. Relevant context is retrieved
5. Prompt is constructed with context
6. LLM generates a structured response
7. Response is returned to the frontend

## Focus Timer Design

Instead of storing timer state in memory, the system stores immutable focus events: start, pause, resume, and stop. Elapsed time is derived dynamically from event history.

This makes the timer stateless, multi-device safe, restart-safe, and horizontally scalable.

## Local Setup
```bash
git clone https://github.com/priyeshkjha/D2_23BCE1221_Priyesh_Kumar_Jha
cd your-repo
npm install
npm run dev
```
EOF