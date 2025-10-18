import 'package:flutter/cupertino.dart';

class VerifierTabSegment extends StatelessWidget {
  static const EdgeInsets _padding = EdgeInsets.all(8.0);
  static const double _spacing = 8.0;
  final IconData icon;
  final String title;
  const VerifierTabSegment({
    super.key,
    required this.icon,
    required this.title,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: _padding,
      child: Row(
        spacing: _spacing,
        children: [
          Icon(icon),
          Text(title),
        ],
      ),
    );
  }
}
