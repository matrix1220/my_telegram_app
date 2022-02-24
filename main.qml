import QtQuick 2.15
import QtQuick.Window 2.2
//import QtQuick.Layouts 1.15

Window {
	title: "my telegram app"
	visible: true
	minimumWidth: 400
	minimumHeight: 500
	MouseArea {
		anchors.fill: parent
		onClicked: app.toggleVisible()
	}
	LoginPhone {}
}
