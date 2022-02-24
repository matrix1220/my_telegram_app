import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ScrollView {
	anchors.fill: parent

    ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
    ScrollBar.vertical.policy: ScrollBar.AsNeeded

	ColumnLayout {
		width: parent.width
		spacing: 2

		Repeater {
			model: 40
			Rectangle {
				Layout.fillWidth: true
				border.color: 'black'
				border.width: 1
				//radius: 4
				anchors.margins: 5 
				height: 32
				Text {
					anchors.centerIn: parent
					text: index
				}
			}
		}

	}

}