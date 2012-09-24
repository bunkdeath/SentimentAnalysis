import Qt 4.7

Component {
    id: container

    Item {
        height: tweetText.paintedHeight+50
        width: parent.width
        clip: true

        id: container

        Rectangle {
            id: blueline
            width: parent.width
            height: 2
            anchors.topMargin: 10
            color: "navy"
        }

        Row {
            spacing: 20
            anchors.top: blueline.bottom
            anchors.margins: 10
            width: parent.width

            Column {
                width: parent.width*(50/100)
                Rectangle {
                    gradient: Gradient {
                        GradientStop {
                            id: gradTop
                            position: 0.150
                            color: "#7de235"

                        }

                        GradientStop {
                            id: gradMid
                            position: 0.610
                            color: "#49e083"
                        }

                        GradientStop {
                            id: gradBot
                            position: 1
                            color: "#456b2f"
                        }
                    }

                    id: tweetbox
                    color: "red"
                    smooth: true
                    radius: 30
                    height: tweetText.height+30
                    width: parent.width
                    anchors {
                        left: parent.left
                        leftMargin: 8
                    }

                    Text {
                        id: tweetText
//                        anchors.top: tweetbox.top
                        anchors.left: tweetbox.left
                        anchors.leftMargin: 20
                        anchors.topMargin:15
                        font.pixelSize: 16
                        clip: true
                        width: parent.width-20
                        wrapMode: Text.WordWrap
                        textFormat: Text.RichText
                        text: model.thing.tweet
                    }
                }
            }

            Column {
                width: parent.width*(10/100)
                Rectangle {
                    gradient: Gradient {
                        GradientStop {
                            id: nbgradTop
                            position: 0.150
                            color: model.thing.nbgrad1
                            //color: "#e25d35"

                        }

                        GradientStop {
                            id: nbgradMid
                            position: 0.610
                            color: model.thing.nbgrad2
                            //color: "#e09249"
                        }

                        GradientStop {
                            id: nbgradBot
                            position: 1
                            color: model.thing.nbgrad3
                            //color: "#6b522f"
                        }
                    }

                    id: naiveBayes
                    color: "red"
                    smooth: true
                    radius: 30
                    height: tweetText.height+30
                    width: parent.width
                    anchors {
                        left: parent.left
                        leftMargin: 8
                    }
                }
            }
            Column {
                width: parent.width*(10/100)
                Rectangle {
                    gradient: Gradient {
                        GradientStop {
                            id: migradTop
                            position: 0.150
                            color: model.thing.migrad1
                            //color: "#ddf3eb"

                        }

                        GradientStop {
                            id: migradMid
                            position: 0.610
                            color: model.thing.migrad2
                            //color: "#49c5e0"
                        }

                        GradientStop {
                            id: migradBot
                            position: 1
                            color: model.thing.migrad3
                            //color: "#2f606b"
                        }
                    }

                    id: maximumEntropy
                    color: "red"
                    smooth: true
                    radius: 30
                    height: tweetText.height+30
                    width: parent.width
                    anchors {
                        left: parent.left
                        leftMargin: 8
                    }
                }
            }
            Column {
                width: parent.width*(10/100)
                Rectangle {
                    gradient: Gradient {
                        GradientStop {
                            id: svmgradTop
                            position: 0.150
                            color: model.thing.svmgrad1
                            //color: "#7de235"

                        }

                        GradientStop {
                            id: svmgradMid
                            position: 0.610
                            color: model.thing.svmgrad2
                            //color: "#49e083"
                        }

                        GradientStop {
                            id: svmgradBot
                            position: 1
                            color: model.thing.svmgrad3
                            //color: "#456b2f"
                        }
                    }

                    id: svm
                    color: "red"
                    smooth: true
                    radius: 30
                    height: tweetText.height+30
                    width: parent.width
                    anchors {
                        left: parent.left
                        leftMargin: 8
                    }
                }
            }
            Column {
                width: parent.width*(10/100)
                Rectangle {
                    gradient: Gradient {
                        GradientStop {
                            id: selfgradTop
                            position: 0.150
                            color: model.thing.selfgrad1
                            //color: "#7de235"

                        }

                        GradientStop {
                            id: selfgradMid
                            position: 0.610
                            color: model.thing.selfgrad2
                            //color: "#49e083"
                        }

                        GradientStop {
                            id: selfgradBot
                            position: 1
                            color: model.thing.selfgrad3
                            //color: "#456b2f"
                        }
                    }

                    id: self
                    color: "red"
                    smooth: true
                    radius: 30
                    height: tweetText.height+30
                    width: parent.width
                    anchors {
                        left: parent.left
                        leftMargin: 8
                    }
                }
            }
        }
        MouseArea {
            id: mouseArea
            anchors.fill: parent
            hoverEnabled: true

            onEntered: {
                mainView.state = "showListViews"
                container.forceActiveFocus()
                mainView.forceActiveFocus()
            }
            onClicked: {
                container.forceActiveFocus()
                selectedTweetNumber = tweetNumber;
            }
        }

        states: [
            State {
                name: "selected"
                when: (tweetNumber==selectedTweetNumber)
                PropertyChanges {target: beerDelegateRectangle; color: "red"}
            },
            State {
                name: "active"; when: container.activeFocus
                PropertyChanges { target: tweetbox; color: "#FCFFF5"; scale: 1.05 }
                PropertyChanges { target: tweetText; font.pixelSize: 16 }
            }
        ]

        transitions: Transition {
            NumberAnimation { properties: "scale"; duration: 300 }
        }
    }
}
