package main

import (
	"reflect"
	"testing"
)

func Test_intersect(t *testing.T) {
	type args struct {
		group        map[int32]bool
		personString string
	}
	tests := []struct {
		name string
		args args
		want map[int32]bool
	}{
		{
			args: args{
				group: map[int32]bool{65: true},
				personString: "ABC",
			},
			want: map[int32]bool{65: true},

		},
		{
			args: args{
				group: map[int32]bool{65: true, 66: true},
				personString: "AC",
			},
			want: map[int32]bool{65: true},

		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := intersect(tt.args.group, tt.args.personString); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("intersect() = %v, want %v", got, tt.want)
			}
		})
	}
}
