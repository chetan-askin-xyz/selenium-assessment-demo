# Setup

## Assignment setup

This repo is the starter for the assignment. When you push your code, an automated assessment runs on your submission. You only need to do **one thing once** before pushing.

## One-time setup: add the trigger secret

Before your first push, add a single secret to this repository so the assessment can be triggered:

1. Open your repo on GitHub.
2. Go to **Settings** → **Secrets and variables** → **Actions**.
3. Click **New repository secret**.
4. **Name:** `ASSESSMENT_TRIGGER_TOKEN`  
   **Value:** use the token your instructor provided (e.g. in class, LMS, or email).
5. Click **Add secret**.

You do this once per repo. Do not share the token or commit it; it stays in GitHub Secrets.

## After setup: just push

- Work on your code (e.g. in the `tests/` folder or as instructed).
- Commit and push to the `main` or `master` branch.
- Each push triggers the assessment. The assessment runs on the instructor’s side; you will not see the result in this repo’s Actions tab. Your instructor will use the results (e.g. from their workflow artifacts or Moodle).

## What’s in this repo

- **`.github/workflows/trigger-assessment.yml`** – Runs on every push to `main`/`master` and notifies the assessment system. You don’t need to edit this file.
- Rest of the repo – assignment instructions, starter code, and your solution (e.g. under `tests/`).

## Troubleshooting

- **Assessment not running?** Make sure you added the secret `ASSESSMENT_TRIGGER_TOKEN` and that you’re pushing to `main` or `master`.
- **Lost or wrong token?** Ask your instructor for the token again and update the secret in Settings → Secrets and variables → Actions.

