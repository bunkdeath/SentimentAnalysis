//import QtQuick 1.1
//Component {
//    Item {
//        clip: true

//        height: tweetText.paintedHeight+60


//        Rectangle {
//            gradient: Gradient {
//                GradientStop {
//                    position: 0.140
//                    color: "#ddf3eb"
//                }

//                GradientStop {
//                    position: 0.590
//                    color: "#49c5e0"
//                }

//                GradientStop {
//                    position: 1
//                    color: "#2f606b"
//                }
//            }

//            id: tweetbox
//            color: "red"
//            smooth: true
//            radius: 30
//            height: tweetText.paintedHeight+40
//            width: parent.width-10
//            anchors {
//                left: parent.left
//                leftMargin: 8
//            }
//        }

//        Text {
//            id: tweetText
//            anchors.fill: parent
//            anchors.leftMargin: 20
//            anchors.topMargin: 20
//            anchors.bottomMargin: 20
//            anchors.rightMargin: 20
//            font.pixelSize: 16
//            clip: true
//            width: parent.width
//            wrapMode: Text.WordWrap
//            textFormat: Text.RichText
//            //        text: "hello from qml, testing for qml twitter model for major project title #SentimentAnalysis hello from qml, testing for qml twitter model for major project title #SentimentAnalysis hello from qml, testing for qml twitter model for major project title #SentimentAnalysishello from qml, testing for qml twitter model for major project title #SentimentAnalysishello from qml, testing for qml twitter model for major project title #SentimentAnalysis "
//            text:tweet
//        }
//    }
//}






import Qt 4.7

Component {
    Item {
        height: tweetText.paintedHeight+50
        width: parent.width
        clip: true

        id: container


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
            height: container.height
            width: parent.width-30
            anchors {
                left: parent.left
                leftMargin: 8
            }
        }

        Image {
            id: realImage;
            source: "images/user3.jpg"
            anchors {
                left: parent.left
                leftMargin: 20
                top: parent.top
                topMargin: 20
                bottomMargin: 20
                rightMargin: 20
            }
            width:70; height:70
        }

        Text {
            id: tweetText
            anchors.top: realImage.top
            anchors.left: realImage.right
            //anchors.bottom: realImage.bottom
            anchors.leftMargin: 20
            anchors.right: tweetbox.right
            anchors.rightMargin: 20
            font.pixelSize: 16
            clip: true
            width: 500
            wrapMode: Text.WordWrap
            textFormat: Text.RichText
            text: "hello from qml, testing for qml twitter model for major project title on  #SentimentAnalysis project title #SentimentAnalysis on on on"
            onLinkActivated: handleLink (link)
        }

        Text {
            anchors.top: tweetText.bottom
            anchors.left: tweetText.left
            anchors.leftMargin: 0
            anchors.bottom: tweetbox.bottom
            anchors.topMargin: 4
            font.pixelSize: 12
            clip: true
            width: tweetText.width
            wrapMode: Text.WordWrap
            textFormat: Text.RichText
            text: "<html><span style=\"color:#779dca\">"+"12:00pm"+" from bunkdeath </span>"
        }

        function handleLink (link) {
            console.log("link: "+link)
            if (link.slice(0,4) == 'http') {
                Qt.openUrlExternally (link);
            }
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            hoverEnabled: true

            onEntered: {
                container.forceActiveFocus()
            }
            onClicked: {
                ListView.view.currentIndex = index
                container.forceActiveFocus()
            }
        }

        states: State {
            name: "active"; when: container.activeFocus
            PropertyChanges { target: tweetbox; color: "#FCFFF5"; scale: 1.05 }
            PropertyChanges { target: tweetText; font.pixelSize: 16 }
        }

        transitions: Transition {
            NumberAnimation { properties: "scale"; duration: 300 }
        }
    }
}
