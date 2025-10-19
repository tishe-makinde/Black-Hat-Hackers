import 'package:flutter/cupertino.dart';
import 'package:trustify_app/features/verification/presentation/widgets/add_image_button.dart';
import 'package:trustify_app/features/verification/presentation/widgets/credibility_semantics.dart';
import 'package:trustify_app/features/verification/presentation/widgets/how_to_use_section.dart';
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
              fontSize: 28.0,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 12.0),
          AddImageButton(),
          const SizedBox(height: 12.0),
          VerifyButton(
            onPressed: () {},
          ),
          const SizedBox(height: 20.0),
          HowToUseSection(
            steps: [
              'Upload a photo to verify',
              'See final credibility semantics',
              'View original image source'
            ],
          ),
          const SizedBox(height: 12.0),
          CredibilitySemantics(),
        ],
      ),
    );
  }
}
