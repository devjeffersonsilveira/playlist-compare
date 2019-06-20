/*
Copyright © 2019 NAME HERE <EMAIL ADDRESS>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package actions

import (
	"fmt"
	"log"

	"github.com/zmb3/spotify"
)

// ListOne return just one playlist data
func ListOne(client *spotify.Client) *spotify.SimplePlaylistPage {
	fmt.Println("listOne called")
	var err error
	var playlists *spotify.SimplePlaylistPage
	playlists, err = client.CurrentUsersPlaylists()
	if err != nil {
		log.Print(err)
	}
	return playlists
}
