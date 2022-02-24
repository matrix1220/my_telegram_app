import QtQuick 2.15
import QtQuick.Controls 2.15

Column {
	visible: app.visible
	spacing: 12
	anchors.verticalCenter: parent.verticalCenter
	anchors.horizontalCenter: parent.horizontalCenter


	Text {
		anchors.horizontalCenter: parent.horizontalCenter
		text: "Phone:"
	}

	TextInput {
		id: input
		font.pointSize: 14
		focus: true
		text: "+"
		validator: RegularExpressionValidator { regularExpression: /\+\d{5,13}/ }
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

	Button {
		anchors.horizontalCenter: parent.horizontalCenter
		text: "Ok"
	}
}