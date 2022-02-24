import QtQuick 2.15
import QtQuick.Controls 2.15


Rectangle {
	anchors.fill: parent

	Column {
		anchors.fill: parent
		spacing: 2
		//anchors.verticalCenter: parent.verticalCenter
		//anchors.horizontalCenter: parent.horizontalCenter

		Repeater {
			model: 40
			Rectangle {
				y: -vbar.position * height * 40 + height * index
				width: parent.width
				border.color: 'black'
				border.width: 1
				radius: 4
				anchors.margins: 5 
				height: 32
				Text {
					anchors.centerIn: parent
					text: index
				}
			}
		}

	}
	ScrollBar {
		id: vbar
        //hoverEnabled: true
        //active: hovered || pressed
        orientation: Qt.Vertical
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        size: 0.5
    }

}