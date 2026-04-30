# PySysTools Architecture

## DevSecOps Release Flow

```mermaid
graph TD
    A[GitHub Repository <br/> main branch] -->|Push / Pull Request| B{GitHub Actions CI}
    B -->|Linting & SAST| C[Code Quality Checks]
    B -->|pytest| D[Unit & Integration Tests]
    C --> E{Merge to main}
    D --> E
```
