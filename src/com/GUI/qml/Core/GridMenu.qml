import Charts 1.0
import Qt 4.7

FocusScope {
    property alias interactive: gridView.interactive

    onActiveFocusChanged: {
        if (activeFocus) 
            mainView.state = ""
    }

    Rectangle {
        anchors.fill: parent
        clip: true
        gradient: Gradient {
            GradientStop { position: 0.0; color: "#193441" }
            GradientStop { position: 1.0; color: Qt.darker("#193441") }
        }

        GridView {
            id: gridView
            anchors.fill: parent; anchors.leftMargin: 20; anchors.rightMargin: 20; anchors.topMargin: 50;
            cellWidth: 300; cellHeight: 300
            focus: true
            model: PieModel{}

            KeyNavigation.down: listMenu
            KeyNavigation.left: contextMenu

            delegate: Item {
                id: container
                width: GridView.view.cellWidth; height: GridView.view.cellHeight

                Piechart{
                    id: pie
                }
/*
Item {
    width: 300; height: 200

    PieChart {
        anchors.centerIn: parent
        width: 200; height: 200

        slices: [
            PieSlice {
                anchors.fill: parent
                color: "red"
                fromAngle: 0; angleSpan: 120
            },
            PieSlice {
                anchors.fill: parent
                color: "green"
                fromAngle: 120; angleSpan: 120
            },
            PieSlice {
                anchors.fill: parent
                color: "blue"
                fromAngle: 240; angleSpan: 120
            }
        ]
    }
}
*/
                /*Rectangle {
                    id: content
                    color: "transparent"
                    smooth: true
                    anchors.fill: parent; anchors.margins: 20; radius: 10

                    Rectangle { color: "#91AA9D"; anchors.fill: parent; anchors.margins: 3; radius: 8; smooth: true }
                    Image { source: "images/qt.png"; anchors.centerIn: parent; smooth: true }
                }*/

                MouseArea {
                    id: mouseArea
                    anchors.fill: parent
                    hoverEnabled: true

                    onEntered: {
                        container.forceActiveFocus()
                    }
                    onClicked: {
                        GridView.view.currentIndex = index
                        container.forceActiveFocus()
                    }
                }

                states: State {
                    name: "active"; when: container.activeFocus
                    PropertyChanges { target: pie; color: "#FCFFF5"; scale: 1.1 }
                }

                transitions: Transition {
                    NumberAnimation { properties: "scale"; duration: 100 }
                }
            }
        }
    }
}
