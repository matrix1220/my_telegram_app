import QtQuick 2.15
import QtQuick.Controls 2.15

Column {
	visible: app.notvisible
	spacing: 12
	anchors.verticalCenter: parent.verticalCenter
	anchors.horizontalCenter: parent.horizontalCenter


	Text {
		anchors.horizontalCenter: parent.horizontalCenter
		text: "Code:"
	}

	TextInput {
		id: input
		font.pointSize: 14
		focus: true
		validator: RegularExpressionValidator { regularExpression: /\+\d{4}/ }
		anchors.horizontalCenter: parent.horizontalCenter
		padding: 4

		Rectangle {
			color: "#00000000"
			anchors.fill: parent
			border.color: 'black'
			border.width: 1
			radius: 4

		}
	}
}