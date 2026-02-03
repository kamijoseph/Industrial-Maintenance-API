# Industrial Maintenance API

A production-oriented REST API for managing industrial equipment, inspections, and maintenance schedules.
Built with FastAPI, SQLAlchemy 2.x, Alembic, and Pydantic, the project follows modern backend engineering practices with strict API contracts, database migrations, and clean domain separation.

This API is designed for **real industrial contexts**—factories, plants, utilities, logistics hubs—where equipment uptime, traceability, and auditability matter.

---

## Core Objectives

The system is built to solve four real problems commonly ignored in CRUD demos:

1. **Equipment lifecycle tracking**
   Equipment is not static data. It has an installation time, inspections, and maintenance events.

2. **Operational traceability**
   Every inspection and maintenance action is linked back to a specific asset.

3. **Strict API contracts**
   Request and response models are enforced at runtime to prevent schema drift.

4. **Schema evolution without data loss**
   Alembic migrations are treated as first-class citizens, not afterthoughts.

---

## Key Features

### Equipment Management

* Create and retrieve industrial equipment assets
* Track installation timestamps
* Enforced uniqueness and indexed lookups where appropriate

### Inspection Logs *(extensible)*

* Designed to support recurring inspection records per equipment
* Clean ORM relationships allow historical analysis

### Maintenance Scheduling *(extensible)*

* Models anticipate preventive and corrective maintenance workflows
* Ready for cron-driven or event-driven scheduling

### Strong Data Integrity

* SQLAlchemy 2.0 typed ORM models
* Pydantic schemas with `from_attributes=True`
* Runtime response validation via FastAPI

---

## API Design Philosophy

This project intentionally avoids “loose” API behavior.

### Cardinality is Explicit

* Collection endpoints return lists
* Single-resource endpoints return single objects
* No ambiguous responses

Example:

* `GET /equipment` → list of equipment
* `GET /equipment/{id}` → one equipment or 404

FastAPI enforces these contracts at runtime to prevent silent failures.

### Errors Are Signals, Not Noise

* 404 means “resource does not exist”
* 422 means “client broke the contract”
* 500 means “developer error”

---

## Database & Migrations

* SQLAlchemy is used in **2.0 declarative mode**
* Alembic handles all schema evolution
* Migration files are version-controlled and required for collaboration

The database schema is considered part of the codebase, not an external dependency.

---

## Technology Stack

* **FastAPI** — async-ready, contract-first API framework
* **SQLAlchemy 2.x** — modern typed ORM
* **Alembic** — deterministic schema migrations
* **Pydantic v2** — strict data validation and serialization
* **Uvicorn** — ASGI server with reload support

---

## Design Decisions (Why Things Are Done This Way)

### Why FastAPI?

* Runtime validation of both input *and output*
* OpenAPI generation without manual effort
* Explicit dependency injection for database sessions

### Why SQLAlchemy 2.x Typed ORM?

* Static reasoning about models
* Cleaner relationships
* Future-proof against legacy patterns

---

## Current Status

* Core equipment CRUD: **complete**
* Database migrations: **stable**
* API contracts: **validated**
* Swagger/OpenAPI docs: **available**

The foundation is solid and ready for expansion.

---

## Planned Extensions

This project is intentionally scoped to grow:

* Authentication & role-based access control
* Inspection severity scoring
* Predictive maintenance hooks (ML-ready)
* Asset downtime analytics
* Event-driven notifications
* Audit logs for compliance

None of these require re-architecting what already exists.

---

## Contribution Notes

This project values:

* Clear API contracts
* Small, explicit changes
* Meaningful migrations
* Zero magic behavior

If it’s not explicit, it’s probably not welcome.

---