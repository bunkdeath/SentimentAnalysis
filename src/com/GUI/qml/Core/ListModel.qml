import Qt 4.7

FocusScope {
    clip: true

    onActiveFocusChanged: {
        if (activeFocus)
            mainView.state = "showListViews"
    }

    ListView {
        id: analysisList
        anchors.fill: parent
        model: twitterListModel
        cacheBuffer: 200
        delegate: ModelGreen{}

        Behavior on y {
            NumberAnimation { duration: 600; easing.type: Easing.OutQuint }
        }
    }

    Rectangle { width: parent.width; height: 1; color: "#D1DBBD" }

    Rectangle {
        y: 1; width: parent.width; height: 10
        gradient: Gradient {
            GradientStop { position: 0.0; color: "#3E606F" }
            GradientStop { position: 1.0; color: "transparent" }
        }
    }

    Rectangle {
        y: parent.height - 10; width: parent.width; height: 10
        gradient: Gradient {
            GradientStop { position: 1.0; color: "#3E606F" }
            GradientStop { position: 0.0; color: "transparent" }
        }
    }
}
