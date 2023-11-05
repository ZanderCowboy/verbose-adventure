// import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:frontend/presentation/home_page.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    // TODO Add Responsive Framework
    return MaterialApp(
      title: 'Calculator Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      darkTheme: ThemeData.dark(),
      home: const HomePage(),
    );
  }
}
