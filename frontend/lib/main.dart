import 'package:flutter/material.dart';
import 'package:frontend/application/app.dart';
import 'package:frontend/data/persistance/db_driver.dart';

Future<void> main() async {
  await DbDriver().driver();
  WidgetsFlutterBinding.ensureInitialized();

  runApp(const App());
}
