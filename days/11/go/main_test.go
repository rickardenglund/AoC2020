package main

import (
	"testing"
)

func Test_cmp(t *testing.T) {
	a := [][]rune{{'a','b'}}
	b := [][]rune{{'a','c'}}

	if cmp(a, b) {
		t.Fail()
	}

	a = [][]rune{{'a','b'}, {'b', 'c'}}
	b = [][]rune{{'a','b'}, {'b', 'c'}}

	if !cmp(a, b) {
		t.Fail()
	}


}
