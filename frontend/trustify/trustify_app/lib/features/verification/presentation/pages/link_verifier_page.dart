import 'package:flutter/cupertino.dart';
import 'package:trustify_app/core/theme/colors.dart';
import 'package:trustify_app/features/verification/presentation/widgets/verify_button.dart';

class LinkVerifierPage extends StatefulWidget {
  static const String _title = 'Misinformation Detector';
  static const EdgeInsets _padding = EdgeInsets.all(16.0);
  const LinkVerifierPage({super.key});

  @override
  State<LinkVerifierPage> createState() => _LinkVerifierPageState();
}

class _LinkVerifierPageState extends State<LinkVerifierPage> {
  final TextEditingController _linkController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);

    return Padding(
      padding: LinkVerifierPage._padding,
      child: Column(
        children: [
          Text(
            LinkVerifierPage._title,
            style: theme.textTheme.textStyle.copyWith(
              fontSize: 28,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 12.0),
          CupertinoTextField(
            controller: _linkController,
            placeholder: 'Paste news article or social media link',
            suffix: CupertinoButton(
              padding: EdgeInsets.zero,
              onPressed: () {},
              child: const Icon(CupertinoIcons.doc_on_doc_fill),
            ),
            cursorColor: AppColors.primary,
          ),
          const SizedBox(height: 12.0),
          VerifyButton(
            onPressed: () {},
          ),
        ],
      ),
    );
  }
}
