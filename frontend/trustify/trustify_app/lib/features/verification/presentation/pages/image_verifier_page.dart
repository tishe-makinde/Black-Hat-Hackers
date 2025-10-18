import 'package:flutter/cupertino.dart';
import 'package:trustify_app/features/verification/presentation/widgets/verify_button.dart';

class ImageVerifierPage extends StatelessWidget {
  static const String _title = 'Fake Image Detector';
  static const EdgeInsets _padding = EdgeInsets.all(16.0);
  const ImageVerifierPage({super.key});

  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);
    return Padding(
      padding: _padding,
      child: Column(
        children: [
          Text(
            _title,
            style: theme.textTheme.textStyle.copyWith(
              fontSize: 28,
              fontWeight: FontWeight.bold,
            ),
          ),
          VerifyButton(
            onPressed: () {},
          ),
        ],
      ),
    );
  }
}
