import Qt 4.7

FocusScope {
    id: container

    property bool open: false

    Item {
        anchors.fill: parent

        Rectangle {
            anchors.fill: parent
            color: "#343434"
            Image { source: "images/stripes.png"; fillMode: Image.Tile; anchors.fill: parent; opacity: 0.3 }
            focus: true
            Keys.onRightPressed: mainView.focus = true
            Column {
                anchors.fill: parent
                spacing: 20
                Column{
                    x: parent.width/2 - 110
                    spacing: 20
                    anchors.leftMargin: 10
                    Text {
                        text: "Search keyword"
                        font.pixelSize: 16; font.bold: true; color: "white"; style: Text.Raised; styleColor: "black"
                        horizontalAlignment: Qt.AlignRight
                    }
                    Input{
                        id: fromIn
                        KeyNavigation.backtab: searchbutton
                        onAccepted:searchbutton.doSearch();
                        focus: true
                    }
                }
                Button {
                    width: 100
                    height: 32
                    x: parent.width - 120
                    id: searchbutton
                    keyUsing: true;
                    opacity: 1
                    text: "Search"
                    KeyNavigation.tab: fromIn
                    Keys.onReturnPressed: searchbutton.doSearch();
                    Keys.onEnterPressed: searchbutton.doSearch();
                    Keys.onSelectPressed: searchbutton.doSearch();
                    Keys.onSpacePressed: searchbutton.doSearch();
                    onClicked: searchbutton.doSearch();

                    function doSearch() {
                        // Search ! allowed
                        if (wrapper.state=="invalidinput")
                            return;

                        screen.focus = true;
                        screen.state = ""
                    }
                }
            }
        }
    }
}
