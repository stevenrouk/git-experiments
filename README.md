# git experiments

Experiments, guided by curiosity, are one of the absolute best ways to learn.

In this repo, I'm conducting some git experiments in order to help me learn about the following:

* Branching strategies
* Stash push / stash pop
* Merge conflicts
* Checking out branches with unfinished work
* git diff
* ...and other things!

The great thing is, with the help of the git documentation (accessed by adding "--help" to the end of a command, like "git stash --help") I can experiment and learn without having to constantly reference StackOverflow or the online documentation.

Here's what I've done so far:

1. Create a new git repo.
2. Create a branch to add the initial hello world function, but purposefully introduce a bug that I'll need to fix later.
3. Merge master into this branch (nothing to merge), then merge the new branch into master.
4. Create another new branch called `primes-func`, to create a function that generates primes.
5. Stash my current work so that I can create a new `bugfix` branch to fix the bug that I purposefully introduced to my original `hello-world` branch.
6. Fix the bug, merge into master.
7. Go back to `primes-func`, merge in my bugfix changes from master.
8. Use `stash pop` to get my work on the primes function back.
9. Complete the function, commit my changes.
10. Before merging these changes into master, create a new `generator-func` branch to create another new function.
11. Create a generator function, then merge it into master.
12. Go back to `primes-func` and merge master into it to get the new changes. Fix the merge conflict, commit the changes, and look at `git log` to see what the commits look like.
13. Finally, merge the `primes-func` branch into master.
14. Write this README!

After going through all of this, I feel like I have a much better handle on all of these commands and the general git workflow.

Remember: experiment, experiment, experiment.
