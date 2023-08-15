// import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:frontend/page_measurements.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.

    const num widthButton = 100.0;
    const num heightButton = 50.0;
    return Scaffold(
      // appBar: AppBar(
      //   // Here we take the value from the MyHomePage object that was created by
      //   // the App.build method, and use it to set our appbar title.
      //   title: Text(widget.title),
      // ),
      body: Stack(
        children: [
          SizedBox( // Bottom Layer
            height: MediaQuery.of(context).size.height * 1.0,
            child: SingleChildScrollView(
              child: Row(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.end,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // constraints: BoxConstraints.loose(const Size(200, 200)),
                    width: MediaQuery.of(context).size.width * 0.8,
                    height: MediaQuery.of(context).size.height * 1.0,
                    transformAlignment: Alignment.centerRight,
                    child: Column( // Body
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisSize: MainAxisSize.max,
                      children: <Widget>[
                        // const Text(
                        //   'You have pushed the button this many times:',
                        //   style: TextStyle(color: Colors.white),
                        // ),
                        // Text(
                        //   '$_counter',
                        //   style: Theme.of(context).textTheme.headlineMedium,
                        // ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ), // Bottom Layer
          SizedBox( // Layer with side bar and items
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height,
            child: Row(
              children: [
                SizedBox( // Side bar
                  width: MediaQuery.of(context).size.width * sideBarWidth,
                  height: MediaQuery.of(context).size.height * sideBarHeight,
                  child: Column( // Side bar
                    mainAxisAlignment: MainAxisAlignment.start,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    mainAxisSize: MainAxisSize.max,
                    children: [
                      // const Text('This is text', style: TextStyle(color: Colors.white),),
                      Container(
                        decoration: BoxDecoration(
                          color: const Color.fromARGB(255, 32, 33, 35),
                          // border: Border.all(width: 1.0, style: BorderStyle.solid),
                        ),
                        height: MediaQuery.of(context).size.height * 1,
                        width: MediaQuery.of(context).size.width * 0.2,
                        child: Column(

                        ),
                      ),
                    ],
                  ),
                ), // Side bar

                SizedBox( // Body Part and items part
                  width: MediaQuery.of(context).size.width * sectionTwoWidth,
                  height: MediaQuery.of(context).size.height * sectionTwoHeight,
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.start,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.max,
                    children: [
                      SizedBox( // Body Part
                        width: MediaQuery.of(context).size.width * bodyWidth,
                        height: MediaQuery.of(context).size.height * bodyHeight,
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          mainAxisSize: MainAxisSize.max,
                          children: [
                            Text('string'),
                          ],
                        ),
                      ),
                      SizedBox( // Items Part
                        width: MediaQuery.of(context).size.width * itemsWidth,
                        height: MediaQuery.of(context).size.height * itemsHeight,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          mainAxisSize: MainAxisSize.max,
                          children: [
                            Container( // Text Field
                              width: 400.0,
                              child: const Padding(
                                padding: EdgeInsets.symmetric(vertical: 8.0, horizontal: 6.0),
                                child: TextField(
                                  style: TextStyle(
                                    color: Colors.white,
                                  ),
                                  decoration: InputDecoration(
                                    border: OutlineInputBorder(),
                                    hintText: 'Enter statement',
                                    hintStyle: TextStyle(
                                      color: Colors.white,
                                    ),
                                  ),
                                ),
                              ),
                            ), // Input box

                            Padding(
                              padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 6.0),
                              child: SizedBox(
                                width: 70.0,
                                height: 50.0,
                                child: ElevatedButton.icon(
                                  onPressed: () => {},
                                  icon: const Icon(Icons.arrow_upward_rounded, size: 24,),
                                  label: Text('')),
                              ),
                            ), // Up Arrow

                            Padding(
                              padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 6.0),
                              child: SizedBox(
                                width: 70.0,
                                height: 50.0,
                                child: ElevatedButton.icon(
                                  icon: const Icon(Icons.send_rounded, size: 24,),
                                  label: Text(''),
                                  onPressed: () {  },
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ), // Layer on top
        ],
      ),

      // Center(
      //   // Center is a layout widget. It takes a single child and positions it
      //   // in the middle of the parent.
      //   child: Column(
      //     // Column is also a layout widget. It takes a list of children and
      //     // arranges them vertically. By default, it sizes itself to fit its
      //     // children horizontally, and tries to be as tall as its parent.
      //     //
      //     // Invoke "debug painting" (press "p" in the console, choose the
      //     // "Toggle Debug Paint" action from the Flutter Inspector in Android
      //     // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
      //     // to see the wireframe for each widget.
      //     //
      //     // Column has various properties to control how it sizes itself and
      //     // how it positions its children. Here we use mainAxisAlignment to
      //     // center the children vertically; the main axis here is the vertical
      //     // axis because Columns are vertical (the cross axis would be
      //     // horizontal).
      //     mainAxisAlignment: MainAxisAlignment.center,
      //     children: <Widget>[
      //       const Text(
      //         'You have pushed the button this many times:',
      //       ),
      //       Text(
      //         '$_counter',
      //         style: Theme.of(context).textTheme.headlineMedium,
      //       ),
      //     ],
      //   ),
      // ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
      backgroundColor: const Color.fromARGB(255, 52, 53, 65),
    );
  }
}