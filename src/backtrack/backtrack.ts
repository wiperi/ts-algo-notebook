type BacktrackArgs<S, C> = {
  state: S;
  choices: Iterable<C>;
  isSolution: (state: S) => boolean;
  recordSolution: (state: S) => void;
  shouldPrune: (state: S, choice: C) => boolean;
  makeChoice: (state: S, choice: C) => void;
  undoChoice: (state: S, choice: C) => void;
};

function func<S, C>({
  state,
  choices,
  isSolution,
  recordSolution,
  shouldPrune,
  makeChoice: updateState,
  undoChoice: revertState,
}: BacktrackArgs<S, C>) {
  function backtrack(state: S) {
    if (isSolution(state)) {
      recordSolution(state);
      return;
    }

    for (const choice of choices) {
      if (shouldPrune(state, choice)) {
        continue;
      }

      updateState(state, choice);
      backtrack(state);
      revertState(state, choice);
    }
  }

  backtrack(state);
}

const res: any = [];

func({
  state: [],
  choices: [1, 2, 3, 4],
  isSolution: state => state.length === 3,
  recordSolution: state => res.push([...state]),
  shouldPrune: (state, choice) => state.includes(choice),
  makeChoice: (state, choice) => state.push(choice),
  undoChoice: (state, choice) => state.pop(),
});

console.log(res);
