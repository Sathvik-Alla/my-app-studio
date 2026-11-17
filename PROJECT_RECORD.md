# IS373 Individual Plan | Sathvik Alla

Plan review due November 17, 2026 at 1 p.m. Eastern. This is the evolving record for the portfolio and Animated Realms Help Desk RAG plan. [Canvas assignment](https://njit.instructure.com/courses/70733/assignments/769188)

### Research review index

| Deliverable | Sources | Comparisons | Decisions | Actual checks |
| --- | --- | --- | --- | --- |
| [Portfolio](#1-portfolio--career-research) | [Employer postings](#employer-postings) · [Work evidence](#responsibilities-and-work-evidence) | [Career directions](#career-directions) · [Layout options](#layout-options) | [Target reader](#portfolio-decision) · [Page outline](#public-page-outline) | [Portfolio checks](#portfolio-actual-checks) |
| [RAG app](#2-rag-app--technical-research) | [Primary documentation](#primary-technical-sources) · [Source manifest](#source-manifest) | [Retrieval methods](#retrieval-comparison) · [Design choices](#bounded-design-choices) | [Stack and limits](#stack-decision) · [Planned trace](#planned-source-walkthrough) | [SQLite smoke check](#rag-actual-checks) · [Planned evaluation](#planned-evaluation) |

## 1. Portfolio + career research

**Changed.** Added three role references, a provisional target and reader, three links from responsibilities to work, and a portfolio outline.

**Checked.** Employer sources and existing project evidence were reviewed on November 16, 2026. See [portfolio actual checks](#portfolio-actual-checks).

**Next.** Confirm the target and case study scope, outline the pages by November 24, and ask a peer to identify the target role, find one supporting artifact and open a featured project. **Peer feedback pending.** Record the actual issue, decision, changed link and retest result once available.

### Employer postings

Source access date for all three is November 16, 2026. Role descriptions below are summaries of the employer postings. Personal career reflection belongs in Canvas.

#### Palantir Technologies · Forward Deployed Software Engineer, New Grad – Commercial

- **Family and location.** Forward-deployed engineering. New York, NY, hybrid full-time. Travel expectation is 25–50% depending on the assignment.
- **Required and eligibility.** Engineering degree, programming proficiency, and graduation in December 2026 or spring 2027. The expected fall 2026 timing listed in the old portfolio is compatible if it means December. Whether the NJIT IT degree meets the degree requirement needs employer confirmation.
- **Preferred and valued.** Examples of preferred degree fields include computer science, engineering, math, physics and data science. The posting values initiative, working through ambiguity and adapting to customer needs.
- **Three responsibilities.** Partner with engineers on architecture, build custom apps or LLM workflows tailored to customer operations, and manage relationships with users and executives.
- **Evidence and gap.** Animated Realms shows a scoped app and an access-control decision with tests. Customer discovery and stakeholder ownership remain an evidence gap. By **November 20**, outline a short demonstration around a user's problem and record one genuine feedback item when available.
- [Employer posting](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728) · [Palantir careers listing](https://www.palantir.com/careers/open-positions/) · [Animated Realms role evidence](https://github.com/Sathvik-Alla/my-app-studio/pull/7)

#### Amazon.com Services LLC · Software Development Engineer, Amazon Leo, Early Career – 2027 (US)

- **Family and location.** Early-career product/platform software engineering. Redmond, WA is listed. Placement depends on business availability.
- **Required and eligibility.** Age 18+, a completed or in-progress bachelor's or master's in a listed or related STEM field, a general-purpose language, data structures/algorithms or object-oriented design experience, and AI-assisted development experience. The posting also specifies an export-control eligibility requirement. Degree fit and individual eligibility require confirmation.
- **Preferred.** Technical project or internship experience, relevant cloud/database/version-control or debugging experience, adaptability, software lifecycle knowledge, and communication and problem-solving skills.
- **Three responsibilities.** Design and build reliable services, produce clear technical documentation, and monitor and troubleshoot production issues.
- **Evidence and gap.** The FastAPI account and role PRs show scoped service changes and checks. CropCast shows DEV readiness documentation. A production monitoring or incident-handling example is the gap. By **November 23**, prepare a repeatable health-check note with expected output and one failure case for the portfolio.
- [Employer posting](https://www.amazon.jobs/en/jobs/10597803/software-development-engineer-amazon-leo-early-career-2027-us) · [FastAPI account changes](https://github.com/Sathvik-Alla/my-app-studio/pull/5) · [CropCast DEV evidence](https://github.com/MattToegel/IT490-TEAM-D-F2026/pull/34)

#### Amazon.com Services LLC · Software Development Engineer Intern – Summer 2027 (USA)

- **Family and location.** Software engineering internship. In-person, full-time, 12 weeks at US sites. The description includes Newark, Jersey City and New York. Placement is subject to availability.
- **Required and eligibility.** Age 18+, current enrollment in a listed or related STEM program, a general-purpose language, data structures/basic algorithms or object-oriented design, AI-assisted development experience, and full-time availability. Degree conferral must fall between October 2027 and September 2029, with at least one academic term remaining afterward. The publicly listed fall 2026 graduation is outside that window if still current.
- **Preferred.** Technical internship or project work, relevant cloud, database or version-control skills, software lifecycle knowledge, communication, adaptability, and evidence of initiative.
- **Three responsibilities.** Break ambiguous problems into implementable parts, review code for correctness including AI-assisted changes, and participate in CI/CD and service operations.
- **Evidence and gap.** APP-002 and APP-003 show staged scope and contract checks. The graduation window is the immediate gap. By **November 19**, confirm the degree conferral date and filter future listings for the corresponding early-career cohort.
- [Employer posting](https://www.amazon.jobs/en/jobs/10552937/software-development-engineer-intern-summer-2027-usa) · [Studio 2 decisions and checks](https://github.com/Sathvik-Alla/my-app-studio/blob/main/SPEC.md#evidence)

### Career directions

| Direction | What the employer emphasizes | Evidence and gap |
| --- | --- | --- |
| Forward-deployed engineering | Customer discovery, adapting software to operational needs, stakeholder communication and end-to-end delivery | Salesforce administration/development training is useful background for discussing business workflows. Animated Realms provides a scoped user-facing example. A real customer-feedback and delivery example is still needed. |
| Backend/platform software engineering | Reliable services, documented changes, code verification and operational troubleshooting | NJIT IT coursework, FastAPI account and role checks, and CropCast DEV verification give the reader concrete artifacts. The RAG build can add retrieval evaluation and a documented hosted workflow. |

### Portfolio decision

**Provisional target** is early-career backend software engineer, with platform and retrieval work as portfolio themes. The primary reader is a backend hiring manager or technical reviewer who should quickly identify the role, open a code or test artifact, and understand what Sathvik contributed. Public background can list NJIT Information Technology and Salesforce administration/development training as reported. The existing resume lists Salesforce skills. A verified credential or training link is still pending. [Existing resume source](https://github.com/Sathvik-Alla/portfolio-website/blob/main/index.html)

### Responsibilities and work evidence

| Employer responsibility | Work to feature and what it shows |
| --- | --- |
| Amazon Leo · build reliable services | [FastAPI role implementation](https://github.com/Sathvik-Alla/my-app-studio/blob/main/app/features/roles.py) and [authorization contracts](https://github.com/Sathvik-Alla/my-app-studio/blob/main/contracts/test_roles.py) show an access boundary checked by direct request. |
| Amazon Leo · write accurate technical documentation | [CropCast PR #34](https://github.com/MattToegel/IT490-TEAM-D-F2026/pull/34) records DEV service readiness and the observed login HTTP result. Repository access is required. The public [Studio 2 evidence table](https://github.com/Sathvik-Alla/my-app-studio/blob/main/SPEC.md#evidence) is a second documentation sample. |
| Amazon intern · break ambiguous work into implementable parts | [Studio 2 decisions](https://github.com/Sathvik-Alla/my-app-studio/blob/main/SPEC.md) describe the staged homepage, accounts, and roles work with acceptance evidence. |

**Own contribution.** Studio 2 records Sathvik's predictions, Chrome observations, interpretation of the same-session role change, and keep decisions. For CropCast, Sathvik recorded and submitted the DEV APP readiness evidence in PR #34 for a shared task. The PR reports that the APP and log-listener services were active and that GET /login returned HTTP 200. Credit team members for their own work and omit claims that Sathvik personally verified QA or production. **AI help.** Studio 2 notes credit AI with implementation assistance and automated checks. Codex found and summarized sources, drafted this plan and proposed the target and layout. [Learner evidence](https://github.com/Sathvik-Alla/my-app-studio/blob/main/LEARNING.md#app-003) · [CropCast changed file](https://github.com/MattToegel/IT490-TEAM-D-F2026/pull/34/files)

### Layout options

Both options use the same target statement, three project summaries, role and evidence lines, code/demo links, résumé, GitHub, LinkedIn and contact link.

- **A. Single scrolling page.** Show the intro and all three full case studies in one page with jump links. Simple to build and browse, with more scrolling as evidence grows.
- **B. Home with case-study pages.** Show target and project summaries immediately, with one page per case. Adds navigation and gives each artifact a direct link.
- **Provisional choice.** B. Keep one sentence for role, contribution and the strongest evidence on each homepage card. Use a consistent problem, contribution, decision, check and link structure on the case pages.

### Public page outline

- **Home.** NJIT IT introduction, target role, evidence-first project links and professional contact. Link public résumé, [GitHub](https://github.com/Sathvik-Alla) and [LinkedIn](https://www.linkedin.com/in/sathvik-alla2). Confirm contact and résumé details before publishing.
- **Animated Realms Help Desk.** Individual RAG case study with permitted sources, retrieval decision, trace, evaluation, code and a labeled app route planned for Build.
- **Group case study.** CropCast is the currently evidenced group portfolio example. Describe the team's goal, then feature Sathvik's DEV readiness evidence and PR. The team repository is private. For a public portfolio, use an approved summary and a shareable artifact only with team permission. Confirm whether CropCast is the IS373 Deliverable 3 system. If it is a separate course project, add the actual IS373 group system and verified personal contribution as a case study once its link is available.
- **Animated Realms Studio 2.** Existing FastAPI homepage, member login/logout and server-side roles. Link to the code and the historical checks.

### Portfolio actual checks

- **Source check, November 16.** Both Amazon posting pages returned full role text and application links. Palantir's official directory listed the role and its employer-authored Lever posting was readable through the search index. Direct automated fetch returned 403. Reopen the Palantir posting in a regular browser during student review.
- **Evidence check, November 16.** GitHub returned the Studio spec, learning notes, role source and role test file. PR #34 lists one changed file, the DEV APP readiness record. Access was verified with the connected account. Peer and instructor access depends on team repository permissions. The existing Studio 2 notes and PR #7 report 401/403/200 for anonymous/member/admin and a same-session promotion/downgrade check. Those are historical results. [Studio 2 check evidence](https://github.com/Sathvik-Alla/my-app-studio/pull/7) · [CropCast evidence](https://github.com/MattToegel/IT490-TEAM-D-F2026/pull/34/files)
- **Planned and unrun.** On the portfolio pages, check that the target and featured evidence are visible without login, links work with keyboard navigation, and content fits a narrow screen. Ask a peer whether Amazon's reliability responsibility actually supports the target reader and featured role-test evidence.

## 2. RAG app + technical research

**Changed.** Defined a technical reader, compared keyword, vector and graph retrieval, selected a provisional stack and prepared a five-note corpus, trace and evaluation.

**Checked.** Reviewed primary technical documentation and ran two keyword fixture assertions. See [RAG actual checks](#rag-actual-checks).

**Next.** By November 24, verify host resources and model access, implement the restricted import and hosted walkthrough, then capture actual retrieval IDs, citations and answers. **Peer feedback pending.** Ask a peer to trace AR-01 and explain what Q3 exposes if either source is absent. Record the actual issue, change and retest when available.

**Purpose and reader.** Animated Realms Help Desk gives a student maintainer quick, sourced answers about sample account and access behavior. The corpus consists of short original demo notes derived from documented Studio 2 behavior. Use only those texts in the prototype corpus.

### Primary technical sources

Reviewed November 16, 2026.

- **FastAPI** provides the Python HTTP application framework. [FastAPI docs](https://fastapi.tiangolo.com/)
- **RAG** supplies retrieved evidence as context for generation. This design adds passage citations and abstention as application behavior. [Original RAG paper](https://arxiv.org/abs/2005.11401)
- **Vector search** represents text as numeric embeddings. pgvector stores and ranks vectors using distances such as cosine distance, with exact search by default and optional approximate indexes. [pgvector documentation](https://github.com/pgvector/pgvector) · [Ollama embedding endpoint](https://docs.ollama.com/api/embed)
- **Property graphs** store entities as labeled nodes and typed connections as relationships. Cypher can match paths that connect entities. [Neo4j graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/)
- **Keyword search** matches tokens and phrases. FTS5 provides MATCH queries and BM25 ranking. [SQLite FTS5](https://www.sqlite.org/fts5.html)
- **Local model serving** uses Ollama's embedding and chat endpoints. Model pages give download and context estimates. [Local FAQ](https://docs.ollama.com/faq) · [Chat endpoint](https://docs.ollama.com/api/chat) · [EmbeddingGemma](https://ollama.com/library/embeddinggemma) · [Qwen2.5](https://ollama.com/library/qwen2.5)

### Retrieval comparison

| Approach | Use in this corpus | Limitation |
| --- | --- | --- |
| SQLite FTS5 keyword baseline | Parameterized MATCH query and BM25 over the same chunks. Good reference for explicit identifiers such as api admin after tokenization. | A rephrased question may miss the right note when its terms differ. |
| PostgreSQL + pgvector | Embed each chunk and question with the same model/configuration, then retrieve the nearest passages by cosine distance. Good candidate for paraphrases. | Similarity can rank related but insufficient passages. Exact strings and versions still need evaluation and metadata. |
| Neo4j property graph | Model Role, Action, Route and Result entities. Example path is Member → REQUESTS → Admin API with an outcome scoped to that role and request. Link the resulting fact to AR-01. Import validated nodes and typed edges with stable IDs and source references. | Multi-hop questions can benefit from explicit edges. A five-note corpus would require manual modeling and edge validation for limited initial gain. |

### Bounded design choices

1. **Chunking.** Compare one coherent chunk per short note against fixed overlapping windows. Start with one note per chunk, preserving its heading and origin. If notes grow, split at headings or paragraph boundaries before considering token windows. Compare expected evidence in top three using Q1–Q4.
2. **Citation display.** Compare a source list at the end with citations attached to individual claims plus expandable excerpts. Choose claim-level citations so a reviewer can verify which passage supports each claim. Remove AR-04 from Q3's retrieved context and check that the answer states what evidence is missing.

### Stack decision

- **Provisional architecture.** Reuse FastAPI for a public question page and a server-restricted import. Store text, manifest metadata and real vectors in private PostgreSQL with pgvector. Use exact cosine search for this tiny corpus. Keep SQLite FTS5 as the comparison experiment over identical inputs. A graph prototype becomes useful if repeated relationship queries cannot be answered reliably from the passages.
- **Hosting and model access.** Start locally. For Build, provision the existing Studio 1 server only if resource and access checks pass. Proxy only the FastAPI web endpoint. Keep PostgreSQL and Ollama private. The Plan has no hosted RAG URL. Use local Ollama with EmbeddingGemma and Qwen2.5 1.5B, recording pulled digests, measured dimensions and runtime settings. Model downloads require network access. Local inference uses no hosted model API key. [Hosting project](https://github.com/Sathvik-Alla/my-server-studio)
- **Cost and storage.** Planned external per-request model spend is $0 with local inference. Existing infrastructure costs and host headroom are unverified. Catalog downloads total about 1.6 GB before runtime overhead. Reserve a provisional 4 GB free disk for models, data and logs, then measure. Use a persistent Postgres volume and keep the versioned source text separately rebuildable. Measure model RAM and latency before choosing the Build host.
- **Request limits.** Proposed caps are 400 characters per question, top three passages, 180 generated tokens, one active inference, five questions per minute per client, 30 seconds per model request, and five UTF-8 notes of at most 10 KiB per import. Return 429 for excess traffic and a clear timeout or unavailable response for model failure. These are application settings to test.

### Source manifest

All five version 1 notes below are original, AI-assisted demo text prepared November 16, 2026 for reuse in this class prototype. The scope is these short notes and their citations. Sources in the Origin column establish factual provenance. No private student data is required.

| ID | Origin | Version | Permission |
| --- | --- | --- | --- |
| AR-01 | [Studio 2 role check](https://github.com/Sathvik-Alla/my-app-studio/pull/7) | 1 | Original demo text for class prototype |
| AR-02 | [Studio 2 account decisions](https://github.com/Sathvik-Alla/my-app-studio/blob/main/SPEC.md#app-002--signup-login-and-logout) | 1 | Original demo text for class prototype |
| AR-03 | [Studio 2 role decisions](https://github.com/Sathvik-Alla/my-app-studio/blob/main/SPEC.md#app-003--server-enforced-roles) | 1 | Original demo text for class prototype |
| AR-04 | [Studio 2 same-session observation](https://github.com/Sathvik-Alla/my-app-studio/blob/main/LEARNING.md#app-003) | 1 | Original demo text for class prototype |
| AR-05 | [Studio 2 account observation](https://github.com/Sathvik-Alla/my-app-studio/blob/main/LEARNING.md#app-002) | 1 | Original demo text for class prototype |

#### AR-01

A signed-in member who requests GET /api/admin receives HTTP 403. A signed-out visitor receives HTTP 401. An administrator receives HTTP 200.

#### AR-02

The home page is open to everyone. The dashboard is private. After sign-out, visiting the dashboard redirects to sign-in.

#### AR-03

New signups create member accounts. The trusted local CLI can promote a member to administrator.

#### AR-04

Protected requests read the current database role. After an administrator is downgraded, the same session loses administrator access on the next protected request.

#### AR-05

Signup requires at least 15 characters in the password. Logout revokes the session on the server.

### Planned source walkthrough

1. **Import.** Read the versioned AR-01 text. Validate the source ID, permission and origin URL. Normalize whitespace and hash the content. An identical reimport leaves the active record unchanged. A changed source gets a new version and replaces old active chunks and vectors atomically, after replacement vectors are ready.
2. **Representation.** Store chunk `AR-01:v1:01`, its exact passage, version, location, model identifier, digest and embedding. Reject input overflow during embedding so text cannot silently disappear. A graph representation could connect the member, route and 403 result with provenance on the fact.
3. **Retrieval.** Embed “What does GET /api/admin return for a signed-in member?” using the import model. Rank active chunks by cosine distance and log returned IDs. Expect AR-01 in the top three. Validate this expectation at Build.
4. **Citation and supported answer.** Provide retrieved passages as evidence to the model. Require citation IDs from the retrieved set and resolve them to the active source passage. Check entailment separately because an ID alone does not prove support. Expected answer is “A signed-in member receives HTTP 403.” [AR-01 passage](#ar-01)
5. **Insufficient evidence.** If passages do not support an answer, return an explanation of what the sources lack. Retrieval score and a model-generated citation can both be wrong.

### Planned evaluation

| ID | Question | Expected evidence and behavior |
| --- | --- | --- |
| Q1 · exact term | What does GET /api/admin return for a signed-in member? | AR-01. Answer 403 with citation. |
| Q2 · paraphrase | I ended my session. Where does the private area send me if I reopen it? | AR-02. Dashboard redirects to sign-in. |
| Q3 · relationship | After an administrator becomes a member, what status should the existing session see on the next GET /api/admin request? | AR-04 establishes the next-request role change and AR-01 supplies 403 for a member. Require both citations. Withhold either source and look for an unsupported status or session claim. |
| Q4 · account rule | What minimum password length does signup require? | AR-05. Answer 15 characters with citation. |
| Q5 · unanswerable | Which credit cards does Animated Realms accept for billing? | No supporting passage. State that the corpus does not answer the question. |

**Observable checks, planned and unrun**

1. Import the five notes twice and verify five active IDs and five chunks, then edit one fixture and verify only its new version is retrieved.
2. Run both retrievers against Q1–Q4 on the same chunks. Save ranked IDs and coverage at three. Vector target is the expected evidence for all four, including both IDs for Q3. Record any misses.
3. Open each displayed citation for Q1–Q4 and verify the cited text supports its claim. Q5 should abstain. Repeat Q3 with each required passage removed in turn and verify the answer reports insufficient support.
4. From a signed-out browser, confirm read-only question access and server-side denial of import. Burst past the request limit and check that excess requests receive 429.
5. After deployment and restart, confirm data persists and run Q1 again. Record the deployed revision, ranked IDs, answer, citation, latency and result.

### RAG actual checks

**November 16, 2026.** Codex inserted the exact five manifest note bodies into an in-memory SQLite 3.50.4 FTS5 table `chunks(id UNINDEXED, body)` and ran parameterized `SELECT id FROM chunks WHERE chunks MATCH ? ORDER BY bm25(chunks)`. Both assertions passed.

| Bound MATCH phrase | Observed rows |
| --- | --- |
| `"api admin"` | `AR-01` only |
| `"billing"` | No rows |

This proves the keyword fixture can distinguish those two terms. The zero-hit result is retrieval evidence for a single phrase. Application import, vector ranking, citations, generated answers, abstention and hosted behavior are still planned.

**Own contribution and AI help.** Sathvik provided the project context, requested one GitHub record and supplied the Canvas briefs. Historical Studio 2 interactions provided the underlying learner observations. Codex drafted the provisional design and note text, reviewed the documentation, and ran the keyword assertions. Student review of the Plan choices and peer feedback are pending.
