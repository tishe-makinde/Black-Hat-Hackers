import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:trustify_app/core/error/exceptions.dart';

abstract interface class VerificationRemoteDataSource {
  Future<Map<String, dynamic>> verifyLink(String url);
  Future<Map<String, dynamic>> verifyImage();
}

class VerificationRemoteDataSourceImpl implements VerificationRemoteDataSource {
  @override
  Future<Map<String, dynamic>> verifyLink(String url) async {
    try {
      final resp = await http.post(
        Uri.parse("http://10.0.2.2:5000/api/analyze"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"url": url}),
      );

      print("Status code: ${resp.statusCode}");

      if (resp.statusCode == 200) {
        final data = jsonDecode(resp.body);
        print("User Info: ${data["user_info"]}");
        print("Related Info: ${data["related_info"]}");
      } else {
        print("Error: ${resp.body}");
      }

      return {};
    } catch (e) {
      print(e);
      throw VerificationException(e.toString());
    }
  }

  @override
  Future<Map<String, dynamic>> verifyImage() {
    // TODO: implement verifyImage
    throw UnimplementedError();
  }
}
