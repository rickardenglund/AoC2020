package main

import (
	"fmt"
	"strings"
	"time"
)

const (
	free     = 'L'
	floor    = '.'
	occupied = '#'
)

func main() {
	start := time.Now()
	fmt.Printf("p1: %v\n", part1(input))
	fmt.Printf("p1 time: %v\n", time.Since(start))
}

func part1(input string) int {
	state := [][]rune{}
	for y, line := range strings.Split(input, "\n") {
		state = append(state, make([]rune, len(line)))
		for x, c := range line {
			state[y][x] = c
		}
	}

	previousState := state
	rounds := 0
	state = nextState(state)
	for !cmp(previousState, state) {
		previousState = state
		state = nextState(state)
		rounds++
	}

	fmt.Printf("rounds: %v\n", rounds)

	count := 0
	for y, line := range strings.Split(input, "\n") {
		for x := range line {
			if state[y][x] == occupied {
				count++
			}
		}
	}

	return count
}

func p(state [][]rune) {
	fmt.Printf("### \n")
	for y := range state {
		for x := range state[y] {
			fmt.Printf("%c", state[y][x])
		}
		fmt.Printf("\n")
	}

}

func cmp(state [][]rune, state2 [][]rune) bool {
	for y := range state {
		for x := range state[y] {
			if state[y][x] != state2[y][x] {
				return false
			}
		}
	}

	return true
}

func nextState(state [][]rune) [][]rune {
	newState := [][]rune{}

	for y := range state {
		newState = append(newState, make([]rune, len(state[0])))
		for x := range state[y] {
			neighbours := countNeighbours(state, x, y)
			newState[y][x] = newValue(state[y][x], neighbours)
		}
	}
	return newState
}

func countNeighbours(state [][]rune, x int, y int) map[rune]int {
	count := map[rune]int{}

	for _, dy := range []int{-1, 0, 1} {
		for _, dx := range []int{-1, 0, 1} {
			if dy == 0 && dx == 0 {
				continue
			}

			curX := x + dx
			if curX < 0 || curX >= len(state[0]) {
				continue
			}

			curY := y + dy
			if curY < 0 || curY >= len(state) {
				continue
			}

			count[state[curY][curX]] += 1

		}
	}

	return count
}

func newValue(current rune, neighbours map[rune]int) rune {
	if current == free && neighbours[occupied] == 0 {
		return occupied
	} else if current == occupied && neighbours[occupied] >= 4 {
		return free
	}

	return current
}

var testInput = `L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL`

var input = `LLLLLL.LL.LL.LLLLLL.LLL.L.LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLL.LL.LLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLL
LLLLLL.LLLLL.LLLL.L.LLLLLLLLLLLLL.LLLLL.LL.LLL.LL.LLLL.LLLLLLLLLLLL.LLLLLLLL.LLLL.L.LLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL..LLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.L.LL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLL.LL.LLLL..
L....L...L...LL..LLL.....L..L..L.L.L..LL..LL......L.L.L..L...L.....LL.......L.L.L..L....L...L....
LLLLLL.LLLLL.LLL.LL..LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLL.LL.LLLLL.LLLLLLLLLLLLL.L..LLL
LLLLLL.LLLLLLLLLLLLLL.L.L.LLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLL.L.LLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLL.L.LLLLLL
LLLLLL.LLLLL.LLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLLL.LLL.LLLLLLLLLLLLLLLL.LLLLLL.L.LL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLLLLLLLL.L.LLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLL.L.LLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLLL
LLLLLL.LLL.L.LLL.LL.LLLLL.L.LLLLL.LLLLLLLLLLLLL.L.LLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLL..LLLLL.LLLLLL
....L.L........L..L.....L.................L.LL...L......LL.L..L.....L.LL...L.L........LLL......L.
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LL.LLLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLLLLLLLLLL.LLLL.LLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLLLLL.LLL.LL.LLLLLLLLLLLLL
LLLLLLLLLLLL.LLLLLL.L.LLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LL.LLLLLLL.L..LLLLLLL.LLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLLLLLLLL.L.LLLLLLLLLLLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLL..LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLL.L
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLL.LLLLLL.LLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLL.LLLLLLL.LLL..L.L.LLLLLL.LLLLLL.LLLLLL
L.LLL....L...L............LL.....LL..LL.L.LLLL.L..L.LL..L.....LLL..L.LLL...L..L.......LLL..L..L..
LL.LLL.LLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.LLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LL.LL.LLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL
LLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLL..LLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLL..LLLLLL
LLLLLL.LLLLLLLLLLLL.L.LLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LLL.LLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLL
LLLLL..LLLLL.LLL.LL.LLLLL.L.L.LLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLLL.L.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLL..LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLL
...L........L..L..L.L.LLL.LL...L..L....L.L.L.L...LLLL..L...L...........LL........L....L..LL....L.
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLL.L.LLLL.LLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLL
LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.LL.LLLL.LL.L.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.L.LLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLL..L...LLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLL.L
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLL.L.LLLLLLLLLLLL.LLLLL.LLL.LLLLLL.LLLLLL
LLLLLLLLLLLLLLL.L.LLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL...LLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLL
..L..L..L..L..LLL....L.LL..L.L..........L.L.L..LLLL...L...LL.L.L........L......LL.L.........L....
LLLLLL.LLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLL.L.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLL.L.LLLL.LLLLLLLL.LLLL.LLLLL.LL.LLLLLL.LLLLL.L..LLLLLLLL.LLLLLLLL.LLLLL..LLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLL..LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.L.LLLLLL.LLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLL.LL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLL...LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLL
L.L..L..L..LL.L...L...LLLLLL.L..L...LL...........L.L..L.........L.L...L.L..L...........L.....L.L.
LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLL..LLLLLLLL.LLLLLL.LLL.LL.LLLLLL
LLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLL..LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLL..LLLLLLLLLL.LLLLLLLL.LLLLLL.LL.LLLLL.LLLL.L.LLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL
L..L...L..LLL...L...L.......LL.......LL.L.L.....LLL....L.L......L.L...L...L.L.L.....L.LL........L
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL..LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.L.LLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL..L.L.LLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL
..LLL..L.......LL.L..........L...L....LL..L.L......LLLLLLL..LLL...L.L.LL..LL...L......L...L.L...L
LLLLL..LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLL.LLLL.LLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLLLLLLL..L.LLLLLLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
.LLLLL.LLLLL.LL.L.L.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL..LLLLLLLLLLLL.LLLLLLLL.LLL.L.L.LLLLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLL
..L.L...L..L.....L...L..L...L.........LL......LL..L..L.L...L....LL.L....L..L.....L....L.L..L.L.LL
LLLLLLLLLLLLLLLLLLL.LLLLL.LL.L.LL.LLLLLLLLLLLLLL..LLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL
L.LLLL.LLLLL.LLLLLL.LLLL..LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.L.LLLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLL
LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLL.LL.LLLLL.LLLLLLLLLLLLL.LL.LLL
.L.....L....L.LL..L.L.......L.LL...L..L.L.LL....LL..L...L.L..L.L.........L...L..LL...LL........L.
LLLLL..LLLLL.LLLLLL.LLLLL.LLLLLLL.LLL.LLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLL.L.LL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.LLL.L.LLLLLL...LLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL..LLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LL.LLL.LLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.L.LLL..LLLLLL
LLLLLL.LLLLL.LLLLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLLLL
LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL
LLLLLL..LLLL.LL.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLLL
LL.LLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LL.LLL
L...L..L.L.........L...L....LLL.........LL...L..L.L....L..LLL...........L...L......LL.L.L..L.....
LLLLLLLLLLLL..LLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLL.L.LLLL.LLLLLLLL.LLL.LLLLLLLL.LL.LLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLL.LLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLL.LL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLL
LLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LL.LLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLL.LLL.LLLLLL.LL.LLLLL.
LLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLL.LL.LLLLL.LLLLLLLLLLLLL.LLLLLL
LL.LL.LLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLL
L.LLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL.LLLLL.
LLLLLL.LLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLL
LLLLL..LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLL.LL
LLLLLL.LLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLL`
