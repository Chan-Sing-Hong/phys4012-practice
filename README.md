# Assignment title

Replace this heading and the placeholders in `report.md` for each assignment.
Put your name and student ID in your **private assignment repository**.

This template contains a small runnable free-fall example to demonstrate the
directory layout, a saved plot, and a physical consistency check. Replace it
with code appropriate to the assignment. It is not a solution to a graded task.

## Run

Use the course's Python 3.12 environment on Linux, macOS, or Ubuntu in WSL.
From the top level of your own repository:

```sh
conda env create --file environment.yml
conda activate phys4012
python -m src.main
python -m unittest discover -s tests -v
```

Create the environment only if it does not already exist. To synchronize an
existing course environment after dependencies change, run `conda env update
--name phys4012 --file environment.yml --prune`. Inside the activated
environment, `python` uses its interpreter. The example writes
`figures/free_fall.png`; open that file to inspect the result. Record any
changed commands and dependencies here so the TA can reproduce your work from
a fresh clone. If you add random sampling, state and record the random seed.

## Layout

- `src/`: the program and reusable functions; avoid putting all the calculation
  inside plotting code.
- `tests/`: a small number of useful checks against independent physical
  predictions, limits, or convergence behaviour.
- `report.md`: assumptions, method, results, and interpretation.
- `figures/`: generated plots, ignored by Git in this starter. To include a
  selected small plot in the report, copy it into a `report-figures/` directory
  and commit that copy.
- `environment.yml`: the Conda environment needed to run the program.

The free-fall test checks conservation of mechanical energy at several times.
An independent physical invariant can detect inconsistent height and velocity
calculations. Passing this one test is not proof that every part of the program
is correct; retain checks that address the actual risks in your assignment.

## Before submission

1. Run the documented command from a fresh shell, and inspect the figures.
2. Check the physics and numerical accuracy; explain a meaningful check in your
   report.
3. Commit the source, report, dependency list, and selected report figures.
4. Push to the private repository designated for this assignment, then inspect
   the latest commit on GitHub. The course instructions specify the deadline
   and submission procedure.

AI assistance is allowed. You must understand and be able to explain the work
you submit, including its assumptions and limitations. Never commit credentials,
access tokens, private keys, or a generated Conda environment.
