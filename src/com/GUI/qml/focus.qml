import Charts 1.0
import QtQuick 1.0
import "Core"

Rectangle {
    id: window
    
    width: 640; height: 480
    color: "#3E606F"

    FocusScope {
        id: mainView

        width: parent.width; height: parent.height
        focus: true

        GridMenu {
            id: gridMenu
            width: parent.width; height: 320

            focus: true
            interactive: parent.activeFocus
        }

        ListModel {
            id: listMenu
            y: 320; width: parent.width; height: parent.height
        }


        Rectangle { 
            id: shade
            anchors.fill: parent
            color: "black"
            opacity: 0 
        }

        states: State {
            name: "showListViews"
            PropertyChanges { target: gridMenu; y: -290 }
            PropertyChanges { target: listMenu; y: 30 }

            PropertyChanges { target: mainView; x: 0 }
            PropertyChanges { target: contextMenu; x: -259; open: false }            
            PropertyChanges { target: shade; opacity: 0 }
        }

        transitions: Transition {
            NumberAnimation { properties: "y"; duration: 600; easing.type: Easing.OutQuint }
        }
    }

    ContextMenu { 
        id: contextMenu; x: -259; width: 260; height: parent.height

        MouseArea {
                anchors.fill: parent; anchors.margins: -10; hoverEnabled: true
                onEntered: contextMenu.focus = true
        }
    }

    

    states: [
        State {
            name: "contextMenuOpen"
            when: !mainView.activeFocus
            PropertyChanges { target: contextMenu; x: 0; open: true }
            PropertyChanges { target: mainView; x: 130 }
            PropertyChanges { target: shade; opacity: 0.25 }
        }
    ]

    transitions: Transition {
        NumberAnimation { properties: "x,opacity"; duration: 600; easing.type: Easing.OutQuint }
    }
}
